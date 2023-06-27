from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from .routes_helpers import validate_model

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")