class DictValidator:
    REQUIRED_KEYS = {'id', 'name', 'status'}

    @staticmethod
    def validate(data):
        return all(key in data and data[key] is not None for key in DictValidator.REQUIRED_KEYS)

if __name__ == '__main__':
    sample_data = {
        'id': 123,
        'name': 'Example',
        'status': 'active'
    }
    print(DictValidator.validate(sample_data))