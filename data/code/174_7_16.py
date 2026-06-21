class KeyFilter:
    REQUIRED_KEYS = ['name', 'age', 'email']

    @staticmethod
    def extract_keys(source_dict):
        return {key: source_dict[key] for key in KeyFilter.REQUIRED_KEYS if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'email': 'alice@example.com',
        'phone': '555-1234'
    }
    filtered_dict = KeyFilter.extract_keys(sample_dict)
    print(filtered_dict)