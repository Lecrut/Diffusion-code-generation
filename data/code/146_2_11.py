class DictSorter:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def sort_by_key(data, key):
        return sorted(data, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorter = DictSorter(sample_data)
    sorted_data_age = sorter.sort_by_key('age')
    print(sorted_data_age)