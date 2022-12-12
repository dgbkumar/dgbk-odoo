# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'academy.course'
    _description = 'Course Info'
    # --------------------------------------- Fields Declaration ----------------------------------