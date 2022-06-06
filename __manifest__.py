# -*- coding: utf-8 -*-
{
    'name': "NATIVA CUSTOM LOGIN",

    'summary': """
        This is a simple app to custome/modified default odoo login page
        """,

    'src': """
        Long src of module's purpose
    """,

    'author': "FEICOM",
    'website': "http://www.nativa-engeeniering.cm",

    'category': 'Themes',
    'version': '1.0',
    'license': 'LGPL-3',
    'support': 'borismeni2@gmail.cm',
    'images': ['static/description/icon.png'],

    'depends': ['base'],

    # always loaded
    'data': [
        'templates/feicom_custom_login_template.xml',
    ],

    'installable' : True,
    'application' : True,

}