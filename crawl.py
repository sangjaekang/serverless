import re
import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='nvmids')
    message = queue.receive_messages(MaxNumberOfMessages=1)[0]
    
    return {
        'statusCode': 200,
        'body': message.body
    }
