# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


#def index():
#    """
#    example action using the internationalization operator T and flash
#   rendered by views/default/index.html or views/generic.html
#
#    if you need a simple wiki simply replace the two lines below with:
#    return auth.wiki()
#    """
#    response.flash = T("Welcome to web2py!")
#    return dict(message=T('Hello World'))
#@auth.requires_login()
def index():
    js = ''
    if len(request.args)>1 and  request.args[-2] == 'new':
        js += '''
        $('#mensagem_data_mensagem__row').hide();
        window.onload = window.setInterval(function() {
            var now = new Date();
            var strDate = [AddZero(now.getDate()), AddZero(now.getMonth() + 1)].join("/");
            var strTime = [AddZero(now.getHours()), AddZero(now.getMinutes())].join(":");
            document.getElementById("mensagem_data_mensagem").value = "Atualizado em " + strDate + " às " + strTime;
        }, 1000);
    
        function AddZero(num) {
            return (num >= 0 && num < 10) ? "0" + num : num + "";
        }
        '''
    elif len(request.args)>1 and request.args[-3] == 'edit':
        js += '''
        $('#mensagem_data_mensagem__row').hide();
        window.onload = window.setInterval(function() {
            var now = new Date();
            var strDate = [AddZero(now.getDate()), AddZero(now.getMonth() + 1)].join("/");
            var strTime = [AddZero(now.getHours()), AddZero(now.getMinutes())].join(":");
            document.getElementById("mensagem_data_mensagem").value = "Atualizado em " + strDate + " às " + strTime;
        }, 1000);
    
        function AddZero(num) {
            return (num >= 0 && num < 10) ? "0" + num : num + "";
        }
        '''
    script = SCRIPT(js, _type='text/javascript')
    db.mensagem.id.readable = False
    grid = SQLFORM.grid(db.mensagem, searchable=False, paginate=25, maxtextlength=70, sortable=False,details=False, csv=False)
    return dict(grid=grid, script=script)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
