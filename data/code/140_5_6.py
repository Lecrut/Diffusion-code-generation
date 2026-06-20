class DataValidator:
    def __init__(self):
        self.required_keys = {'id', 'name', 'status'}

    def validate(self, data):
        return all(key in data and data[key] is not None for key in self.required_keys)

if __name__ == '__main__':
    validator = DataValidator()
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validator.validate(sample_data))