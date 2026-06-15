class DictionaryMerger:
    def merge_dictionaries(self, list_of_dicts):
        merged_dict = {}
        for d in list_of_dicts:
            for key, value in d.items():
                if key in merged_dict and isinstance(merged_dict[key], list):
                    merged_dict[key].append(value)
                else:
                    merged_dict[key] = value
        return merged_dict
if __name__ == '__main__':
    merger = DictionaryMerger()
    sample_data = [
        {'a': 1, 'b': 'hello'},
        {'a': 2, 'c': 3},
        {'b': 'world', 'd': 4},
        {'a': 3, 'e': 5}
    ]
    result = merger.merge_dictionaries(sample_data)
    print(result)