class DictSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        return sorted(self.data, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorter = DictSorter(sample_data)
    sorted_by_age = sorter.sort_by_key('age')
    print(sorted_by_age)