import json
import boto3


def lambda_handler(event, context):
    try:
        destination_bucket = 'user-data-project-aws'
        user_data = event
        if 'SSN' not in user_data.keys():
            print('Error. Missing SSN Value. SSN is mandatory')
            return json.dumps({"Status": "Error", "Reason": "Missing SSN value"})

        
        file_name = str(user_data.get('SSN')) + '.json'
        s3_resource = boto3.resource('s3')

        
        object_handler = s3_resource.Object(destination_bucket, file_name)

        
        object_handler.put(Body=bytes(json.dumps(user_data), encoding='utf-8'))
        

        return json.dumps({"Status": "Success"})

    except Exception as e:
        print("Error Occur while processing data.")
        print(e)
        return json.dumps({"Status": "Error", "Reason": str(e)})
