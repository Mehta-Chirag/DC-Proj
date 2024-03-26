from django import forms
from django_ckeditor_5.fields import CKEditor5Field  # Import CKEditor5Field
from .models import *

class ChapterForm(forms.ModelForm):
    content = CKEditor5Field()  # Use CKEditor5Field for the content field

    class Meta:
        model = Chapter
        fields = ["number", "title", "content", "course"]

    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)  # Corrected super call
        self.fields["course"].queryset = Course.objects.all()


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description", "subject", "image"]

    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)
        self.fields["subject"].queryset = Subject.objects.all()
