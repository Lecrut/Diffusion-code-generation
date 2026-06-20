class DataValidator:
    REQUIRED_KEYS = {'id', 'name', 'status'}

    def validate_data(self, data):
        return all(key in data and data[key] is not None for key in self.REQUIRED_KEYS)

if __name__ == '__main__':
    validator = DataValidator()
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(validator.validate_data(sample_data))