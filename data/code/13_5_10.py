class SafeAttributeFetcher:
    def __init__(self, data_dict):
        for key, value in data_dict.items():
            setattr(self, key, value)

    def get_safe(self, attr_name):
        try:
            return getattr(self, attr_name)
        except AttributeError:
            return None

if __name__ == '__main__':
    sample_data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    obj = SafeAttributeFetcher(sample_data)
    result_existing = obj.get_safe('name')
    result_missing = obj.get_safe('country')
    print(result_existing)
    print(result_missing)