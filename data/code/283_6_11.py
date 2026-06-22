class DictionaryVerifier:
    @staticmethod
    def is_dictionary(element):
        return isinstance(element, dict)

    @staticmethod
    def count_non_dictionaries(data):
        non_dict_count = sum(not DictionaryVerifier.is_dictionary(x) for x in data)
        return non_dict_count

if __name__ == '__main__':
    sample_data1 = [1, 2, {'a': 3}, 'string']
    sample_data2 = [{'x': 5}, {'y': 6}, {}, {'z': 7}]
    print(f"Non-dictionary count in sample_data1: {DictionaryVerifier.count_non_dictionaries(sample_data1)}")
    print(f"Non-dictionary count in sample_data2: {DictionaryVerifier.count_non_dictionaries(sample_data2)}")