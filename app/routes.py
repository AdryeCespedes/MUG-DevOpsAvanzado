from flask import Flask, request, jsonify, send_file, render_template
from app import app
from app.services.scraper import Scraper
from app.services.translator_azureai import Translator_azure
from app.services.markdown_ft import Convertmarkdown
from app.services.translator_gcp import Translator_gcp
import time
import logging
import os 


# Configure logging
logging.basicConfig(level=logging.DEBUG)
output_dir = os.getenv("FLASK_OUTPUT_DIR", "/app/outputs") ## Default for local tests:"/app/outputs" ||  "/home" for Linux App Service Web App

# Serve only img.png from the mounted storage
@app.route('/mnt/sa_mount/img.png')
def serve_image():
    storage_path = '/mnt/sa_mount'
    filename = 'img.png' # Hardcoded filename
    return send_from_directory(storage_path, filename)

