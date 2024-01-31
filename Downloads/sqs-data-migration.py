import boto3

# Create an SQS client for Singapore region
sqs_singapore = boto3.client('sqs', region_name='ap-southeast-1')

# Create an SQS client for Mumbai region
sqs_mumbai = boto3.client('sqs', region_name='ap-south-1')

# Receive messages from Singapore SQS queue
response = sqs_singapore.receive_message(
    QueueUrl='YOUR_SINGAPORE_QUEUE_URL',
    AttributeNames=['All'],
    MaxNumberOfMessages=10
)

messages = response.get('Messages', [])

# Store messages locally or in temporary storage like S3

# Switch to Mumbai region
sqs_mumbai = boto3.client('sqs', region_name='ap-south-1')

# Send messages to Mumbai SQS queue
for message in messages:
    sqs_mumbai.send_message(
        QueueUrl='YOUR_MUMBAI_QUEUE_URL',
        MessageBody=message['Body']
        # Add other message attributes as needed
    )
    # Delete the message from the Singapore SQS queue
    sqs_singapore.delete_message(
        QueueUrl='YOUR_SINGAPORE_QUEUE_URL',
        ReceiptHandle=message['ReceiptHandle']
    )
