import json
import urllib.parse

def lambda_handler(event, context):
    try:
        # Decode URL-encoded form data
        body = urllib.parse.parse_qs(event['body'])
        user = body.get('username', [''])[0]
        pwd = body.get('password', [''])[0]

        if user == 'admin' and pwd == 'pass':
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Welcome'})
            }
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Denied'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error', 'details': str(e)})
        }
