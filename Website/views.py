from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db



views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    else:
        return render_template("index.html")

