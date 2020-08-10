import boto3
s3 = boto3.resource('s3')
obj = s3.object(firstbucketforpractice, example.txt)
body = obj.get()['Body'].read()
print(body)
