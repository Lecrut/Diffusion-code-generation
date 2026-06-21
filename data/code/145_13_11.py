def validate_data(data, schema):
    if isinstance(schema, dict):
        for key, value in schema.items():
            if key not in data:
                return False
            if not validate_data(data[key], value):
                return False
    elif isinstance(schema, list):
        if not all(isinstance(item, type) for item in schema):
            return False
        if not all(isinstance(item, dict) for item in data):
            return False
        if len(data) != len(schema):
            return False
        for i, value in enumerate(schema):
            if not validate_data(data[i], value):
                return False
    elif isinstance(schema, type):
        return isinstance(data, schema)
    else:
        raise ValueError("Invalid schema")
    return True

if __name__ == '__main__':
    sample_data = {
        "user": {
            "id": 123,
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        "roles": [
            {"role_id": 1, "role_name": "admin"},
            {"role_id": 2, "role_name": "user"}
        ]
    }
    
    sample_schema = {
        "user": {
            "id": int,
            "name": str,
            "email": str
        },
        "roles": [
            {"role_id": int, "role_name": str}
        ]
    }
    
    print(validate_data(sample_data, sample_schema))