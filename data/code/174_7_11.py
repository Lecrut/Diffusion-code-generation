class DictionaryFilter:
    def __init__(self, required_keys):
        self.required_keys = required_keys

    def filter_dictionary(self, source_dict):
        return {key: source_dict[key] for key in self.required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    required_keys = ['a', 'c']
    filter_instance = DictionaryFilter(required_keys)
    filtered_result = filter_instance.filter_dictionary(sample_dict)
    print(filtered_result)