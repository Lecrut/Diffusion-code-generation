import operator

class DictionarySorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        return sorted(self.data, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorter = DictionarySorter(sample_data)
    sorted_by_name = sorter.sort_by_key('name')
    sorted_by_age = sorter.sort_by_key('age')
    
    print(sorted_by_name)
    print(sorted_by_age)