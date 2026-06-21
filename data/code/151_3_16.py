class DictMerger:
    def __init__(self, list1, list2, key):
        self.list1 = list1
        self.list2 = list2
        self.key = key

    def merge_dicts(self):
        dict1 = {item[self.key]: item for item in self.list1}
        dict2 = {item[self.key]: item for item in self.list2}
        merged_dict = {**dict1, **dict2}
        return [merged_dict[k] for k in sorted(merged_dict.keys())]

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 3, 'name': 'Charlie'}]
    sample_list2 = [{'id': 2, 'age': 25}, {'id': 3, 'age': 30}]
    merger = DictMerger(sample_list1, sample_list2, 'id')
    merged_result = merger.merge_dicts()
    print(merged_result)