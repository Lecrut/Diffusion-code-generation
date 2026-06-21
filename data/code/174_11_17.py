class DictionaryMerger:
    @staticmethod
    def merge_dictionaries(dict1, dict2):
        merged_dict = {}
        for key in set(dict1) | set(dict2):
            merged_dict[key] = (dict1.get(key, 0) + dict2.get(key, 0))
        return merged_dict

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 3, 'c': 4, 'd': 5}
    result = DictionaryMerger.merge_dictionaries(dict_a, dict_b)
    print(result)