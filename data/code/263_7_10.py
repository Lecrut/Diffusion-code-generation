class DictionaryMerger:
    @staticmethod
    def merge_dictionaries(dict1, dict2):
        result = {}
        keys_to_process = set(dict1) & set(dict2)
        for key in keys_to_process:
            result[key] = dict1[key] + dict2[key]
        return result

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    merged_result = DictionaryMerger.merge_dictionaries(sample_dict1, sample_dict2)
    print(merged_result)