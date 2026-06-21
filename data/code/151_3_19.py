class ListMerger:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def merge_by_key(self, key):
        dict1 = {item[key]: item for item in self.list1}
        dict2 = {item[key]: item for item in self.list2}
        merged_dict = {**dict1, **dict2}
        return [merged_dict[k] for k in sorted(merged_dict.keys())]

if __name__ == '__main__':
    sample_list1 = [{'id': 1, 'name': 'Alice'}, {'id': 3, 'name': 'Charlie'}]
    sample_list2 = [{'id': 2, 'age': 25}, {'id': 3, 'age': 30}]
    merger = ListMerger(sample_list1, sample_list2)
    merged_result = merger.merge_by_key('id')
    print(merged_result)