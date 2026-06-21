def validate_data(data, schema):
    if isinstance(schema, dict):
        return all(validate_data(data.get(key), value) for key, value in schema.items())
    elif isinstance(schema, list):
        return all(validate_data(item, schema[0]) for item in data)
    elif callable(schema):
        return schema(data)
    else:
        return isinstance(data, schema)

if __name__ == '__main__':
    sample_data = {
        'user': {
            'name': 'John Doe',
            'age': 30,
            'email': 'john.doe@example.com'
        },
        'address': {
            'street': '123 Elm St',
            'city': 'Somewhere',
            'zip': '12345'
        }
    }

    schema = {
        'user': {
            'name': str,
            'age': (int, lambda x: 0 <= x <= 120),
            'email': (str, lambda x: '@' in x)
        },
        'address': {
            'street': str,
            'city': str,
            'zip': (str, lambda x: len(x) == 5)
        }
    }

    print(validate_data(sample_data, schema))