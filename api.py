#!/usr/local/python3.7/bin python3
__author__ = '无崖子'
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/ip')
def demo():
    ip = request.remote_addr
    return jsonify({'result': {'ip': ip}})