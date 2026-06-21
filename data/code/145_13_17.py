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
            'name': 'John Doe',
            'age': 30,
            'email': 'john.doe@example.com'
        },
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zip': '12345'
        }
    }

    schema = {
        'user': {
            'name': str,
            'age': lambda x: isinstance(x, int) and 0 < x < 150,
            'email': lambda x: '@' in x
        },
        'address': {
            'street': str,
            'city': str,
            'zip': lambda x: len(x) == 5 and x.isdigit()
        }
    }

    print(validate_data(sample_data, schema))