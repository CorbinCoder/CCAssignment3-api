from flask import Flask, jsonify
from botocore.exceptions import ClientError
import boto3
import config
import logging

application = Flask(__name__)

resource = boto3.resource('dynamodb', region_name=config.region_name, 
                          aws_access_key_id=config.aws_access_key_id, 
                          aws_secret_access_key=config.aws_secret_access_key)

@application.route('/users', methods=['GET'])
def get_users():
    table = resource.Table('users')
    try:
        response = table.scan()
        users = response['Items']
        return jsonify(users)
    except ClientError as e:
        logging.error(e)
        return None
    
@application.route('/posts', methods=['GET'])
def get_posts():
    table = resource.Table('posts')
    try:
        response = table.scan()
        posts = response['Items']
        return jsonify(posts)
    except ClientError as e:
        logging.error(e)
        return None
    
@application.route('/comments', methods=['GET'])
def get_comments():
    table = resource.Table('comments')
    try:
        response = table.scan()
        comments = response['Items']
        return jsonify(comments)
    except ClientError as e:
        logging.error(e)
        return None
    
@application.route('/friends', methods=['GET'])
def get_friends():
    table = resource.Table('friends')
    try:
        response = table.scan()
        friends = response['Items']
        return jsonify(friends)
    except ClientError as e:
        logging.error(e)
        return None
    
@application.route('/likes', methods=['GET'])
def get_likes():
    table = resource.Table('likes')
    try:
        response = table.scan()
        likes = response['Items']
        return jsonify(likes)
    except ClientError as e:
        logging.error(e)
        return None

@application.route('/')
def hello_world():
    return 'Lookbook - API'

if __name__ == "__main__":
    application.run()