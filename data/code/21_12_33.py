class DictSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        return sorted(self.data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorter = DictSorter(sample_data)
    sorted_data_by_age = sorter.sort_by_key('age')
    print(sorted_data_by_age)

    sample_data_2 = [
        {'name': 'David', 'score': 85},
        {'name': 'Eve', 'score': 90},
        {'name': 'Frank', 'score': 78}
    ]
    sorter_2 = DictSorter(sample_data_2)
    sorted_data_by_score = sorter_2.sort_by_key('score')
    print(sorted_data_by_score)