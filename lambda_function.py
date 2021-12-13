import boto3

print('Loading function')

s3 = boto3.client('s3')
sns = boto3.client('sns')


def lambda_handler(event, context):
    # Get object - this is the s3 bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # Get the key - this is the file name
    key = event['Records'][0]['s3']['object']['key']
    
    # Get response
    response = s3.get_object(Bucket=bucket, Key=key)
    
    # Read the  file content
    file_content = str(response['Body'].read())
    words = file_content.split()
    total_words = len(words)
    message = "The word count in the file {} is {}".format(key, total_words)
    # Send email
    sns_response = sns.publish(
        TargetArn='Your SNS ARN HERE',
        Message=message,
        Subject="Word Count Result"
    )
