import operator
SORT_KEY = 'name'

def sort_dictionaries_by_key(dict_list):
    return sorted(dict_list, key=operator.itemgetter(SORT_KEY))
if __name__ == '__main__':
    sample_dicts = [{'name': 'banana', 'color': 'yellow'}, {'name': 'apple', 'color': 'red'}, {'name': 'cherry', 'color': 'red'}]
    sorted_dicts = sort_dictionaries_by_key(sample_dicts)
    print(sorted_dicts)