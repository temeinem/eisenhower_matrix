from odoo import models, fields

class TaskMatrix(models.Model):
    _name = 'task.matrix'
    _description = 'Task Matrix'
    
    name = fields.Char('Name', required=True)
    urgent = fields.Boolean('Urgent')
    important = fields.Boolean('Important')
    category = fields.Char('Category', compute='_compute_category')

    def _compute_category(self):
        for task in self:
            if task.urgent and task.important:
                task.category = 'Do'
            elif not task.urgent and task.important:
                task.category = 'Schedule'
            elif task.urgent and not task.important:
                task.category = 'Delegate'
            else:
                task.category = 'Eliminate'

