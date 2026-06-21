def validate_data(data, schema):
    if not isinstance(data, dict):
        return False
    for key, value in schema.items():
        if key not in data:
            return False
        expected_type = value['type']
        nested_schema = value.get('schema')
        if nested_schema is not None:
            if not validate_data(data[key], nested_schema):
                return False
        elif not isinstance(data[key], expected_type):
            return False
    return True

class DataValidator:

    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        return validate_data(data, self.schema)
if __name__ == '__main__':
    schema = {'name': {'type': str}, 'age': {'type': int, 'schema': {'min': {'type': int, 'value': 0}}}, 'is_student': {'type': bool}, 'courses': {'type': list, 'schema': {'name': {'type': str}, 'credits': {'type': int, 'schema': {'min': {'type': int, 'value': 0}}}}}}
    validator = DataValidator(schema)
    data1 = {'name': 'John Doe', 'age': 25, 'is_student': True, 'courses': [{'name': 'Math', 'credits': 3}, {'name': 'Science', 'credits': 4}]}
    data2 = {'name': 'Jane Smith', 'age': -10, 'is_student': False}
    print(validator.validate(data1))
    print(validator.validate(data2))