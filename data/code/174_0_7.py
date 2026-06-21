class DictMerger:
    @staticmethod
    def merge_dicts(dict1, dict2):
        return {**dict1, **dict2}

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 3, 'c': 4}
    merged_dict = DictMerger.merge_dicts(dict_a, dict_b)
    print(merged_dict)