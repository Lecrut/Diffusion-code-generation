import operator

class DictSorter:
    def __init__(self, key):
        self.key = key
    
    def sort_dicts(self, dict_list):
        return sorted(dict_list, key=operator.itemgetter(self.key))

if __name__ == '__main__':
    sorter = DictSorter('age')
    sample_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    sorted_list = sorter.sort_dicts(sample_list)
    print(sorted_list)