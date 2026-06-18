class DictionaryMerger:
    def merge_dictionaries(self, list_of_dicts):
        merged_dict = {}
        for d in list_of_dicts:
            for key, value in d.items():
                if key in merged_dict:
                    merged_dict[key] = merged_dict[key] + value
                else:
                    merged_dict[key] = value
        return merged_dict
if __name__ == '__main__':
    merger = DictionaryMerger()
    data1 = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
    data2 = [{'c': 5, 'd': 6}, {'a': 10, 'b': 7}]
    list1 = data1 + data2
    result = merger.merge_dictionaries(list1)
    print(result)