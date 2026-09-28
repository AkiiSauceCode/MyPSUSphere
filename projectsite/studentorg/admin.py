from django.contrib import admin

from .models import Collage, Program, Organization, Student, OrgMember

admin.site.register(Collage)
admin.site.register(Program)
admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(OrgMember)