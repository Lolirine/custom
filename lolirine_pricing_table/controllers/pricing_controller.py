from odoo import http
from odoo.http import request

class PricingBoxes(http.Controller):
    @http.route('/pricing-boxes', type='http', auth='public', website=True)
    def pricing_boxes(self, **kwargs):
        products = request.env['product.template'].sudo().search([('categ_id.name', '=', 'Garde-meubles')])
        return request.render('lolirine_pricing_table.pricing_template', {
            'products': products
        })
