import boto3
import pymongo

MONGO_URI = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)

client = boto3.client(
    's3',
    aws_access_key_id="AKIAF6BAFJKR45SAWSZ5",
    aws_secret_access_key="dfansoeifnasdfmaklsfuhlrnfaweiohc",
    aws_session_token="dfnawuhchabcasjndjhvkygbnnreaoengsgl"
)
