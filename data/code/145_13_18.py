def validate_data(data, schema):
    if isinstance(schema, dict):
        for key, value in schema.items():
            if key not in data:
                return False
            if not validate_data(data[key], value):
                return False
    elif isinstance(schema, list):
        for item in data:
            if not validate_data(item, schema[0]):
                return False
    elif callable(schema):
        return schema(data)
    else:
        return isinstance(data, schema)
    return True

if __name__ == '__main__':
    sample_data = {
        'user': {
            'id': 123,
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        },
        'roles': ['admin', 'user']
    }
    
    schema = {
        'user': {
            'id': int,
            'name': str,
            'email': lambda x: '@' in x
        },
        'roles': list
    }
    
    print(validate_data(sample_data, schema))