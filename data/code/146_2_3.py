class DictSorter:
    def __init__(self, dicts):
        self.dicts = dicts

    def sort_by_key(self, key):
        return sorted(self.dicts, key=lambda d: d.get(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorter = DictSorter(sample_dicts)
    sorted_dicts_age = sorter.sort_by_key('age')
    print(sorted_dicts_age)