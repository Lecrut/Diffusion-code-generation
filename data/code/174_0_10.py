class DictMerger:
    def merge_dicts(self, dict1, dict2):
        return {**dict1, **dict2}

if __name__ == '__main__':
    merger = DictMerger()
    merged_dict = merger.merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
    print(merged_dict)