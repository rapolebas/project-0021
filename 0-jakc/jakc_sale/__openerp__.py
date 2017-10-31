# -*- coding: utf-8 -*-

{
    'name': 'Jakc Labs - Workshop Work Order',
    'version': '9.0.0.1.0',
    'category': 'Workshop',
    'license': 'AGPL-3',
    'summary': 'Workshop Work Order',
    'author': "Jakc Labs",
    'website': 'http://www.jakc-labs.com/',
    'depends': [
        'account',
        'sale',
        'hr',
        'mrp',
        'mrp_operations',
        'mrp_hook',
        'mrp_operations_extension',
        'jakc_workshop',
    ],
    'data': [
        'wizard/add_operator_view.xml',
        'wizard/add_image_view.xml',
        'wizard/add_material_view.xml',
        'wizard/process_operator_fee_view.xml',
        'wizard/stock_move_view.xml',
        'views/jakc_sale_view.xml',
        'views/jakc_sale_report.xml',
        'views/jakc_sale_dashboard.xml',
        'views/jakc_product_view.xml',
        'views/templates.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/hr_view.xml',
        'views/mrp_workflow.xml',
        'wizard/report_operator_fee_view.xml',
        'security/ir.model.access.csv',
        'report/report_account_invoice_summary.xml',
        'report/report_account_invoice_summary_templates.xml',
        'report/report_account_invoice_or.xml',
        'report/report_account_invoice_or_templates.xml',
        'report/report_car_status.xml',
        'report/report_car_status_templates.xml',
        'report/sale_order_workshop_report.xml',
        'report/sale_order_workshop_report_templates.xml',
        'report/report_operator_fee_template.xml',

    ],
    'installable': True,
    'application': True,
}
