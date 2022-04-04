
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.widgets import TextArea

image_types = ['jpg', 'png', 'jpeg', 'gif', 'svg', 'webp']

class UploadForm(FlaskForm):
    description = StringField('Description', validators=[InputRequired()], widget=TextArea())
    photo = FileField('Photo', validators=[FileAllowed(image_types, 'Image only!'), FileRequired('File was empty!')])