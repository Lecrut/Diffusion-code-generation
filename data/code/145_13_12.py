def validate_data(data, schema):
    if isinstance(schema, dict):
        return all(validate_data(data.get(key), value) for key, value in schema.items())
    elif isinstance(schema, list):
        return all(isinstance(item, schema[0]) for item in data)
    else:
        return isinstance(data, schema)

if __name__ == '__main__':
    sample_data = {
        'user': {
            'id': 123,
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        },
        'roles': ['admin', 'user']
    }
    
    sample_schema = {
        'user': {
            'id': int,
            'name': str,
            'email': str
        },
        'roles': [str]
    }
    
    print(validate_data(sample_data, sample_schema))