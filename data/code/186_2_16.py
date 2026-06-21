import operator

class DictSorter:
    DEFAULT_KEY = 'name'

    @staticmethod
    def sort_dicts(dict_list, key=DEFAULT_KEY):
        return sorted(dict_list, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = DictSorter.sort_dicts(sample_data)
    print(sorted_data)