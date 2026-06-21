class DictSorter:
    def sort_dicts_by_key(self, dicts, key):
        return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sorter = DictSorter()
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_data = sorter.sort_dicts_by_key(sample_data, 'age')
    print(sorted_data)