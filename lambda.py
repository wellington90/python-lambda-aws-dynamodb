import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NomeSobrenome')

def lambda_handler(event, context):
    nome = event['nome']
    sobrenome = event['sobrenome']
    
    table.put_item(
        Item={
            'nome': nome,
            'sobrenome': sobrenome
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'Nome e sobrenome cadastrados com sucesso!'
    }
