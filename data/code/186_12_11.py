class DictSorter:
    def sort_list(self, dict_list, key):
        return sorted(dict_list, key=lambda x: x.get(key))

if __name__ == '__main__':
    sorter = DictSorter()
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sorter.sort_list(sample_dicts, 'age')
    print(sorted_dicts)