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
    data1 = [{'a': 1, 'b': 2}, {'a': 3, 'c': 4}]
    data2 = [{'b': 5, 'd': 6}, {'a': 7, 'b': 8}]
    data3 = [{'e': 9}]
    all_data = data1 + data2 + data3
    result = merger.merge_dictionaries(all_data)
    print(result)