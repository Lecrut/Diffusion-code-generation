class DictionaryMerger:
    def merge_dictionaries(self, list_of_dicts):
        merged_dict = {}
        for d in list_of_dicts:
            for key, value in d.items():
                if key in merged_dict:
                    if isinstance(merged_dict[key], list):
                        merged_dict[key].append(value)
                    else:
                        merged_dict[key] = [merged_dict[key], value]
                else:
                    merged_dict[key] = value
        return merged_dict
if __name__ == '__main__':
    merger = DictionaryMerger()
    sample_data = [
        {'a': 1, 'b': 2},
        {'b': 3, 'c': 4},
        {'a': 5, 'd': 6},
        {'c': 7}
    ]
    result = merger.merge_dictionaries(sample_data)
    print(result)