from operator import itemgetter

class DictSorter:
    def __init__(self, key):
        self.key = key

    def sort_dicts(self, dict_list):
        return sorted(dict_list, key=itemgetter(self.key))

if __name__ == '__main__':
    sorter = DictSorter('age')
    sample_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    sorted_dicts = sorter.sort_dicts(sample_dicts)
    print(sorted_dicts)