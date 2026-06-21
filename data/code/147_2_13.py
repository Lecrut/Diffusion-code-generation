import operator

SORT_KEY = 'name'

def sort_dicts_by_key(dicts):
    return sorted(dicts, key=operator.itemgetter(SORT_KEY))

if __name__ == '__main__':
    sample_data = [
        {'name': 'banana', 'color': 'yellow'},
        {'name': 'apple', 'color': 'red'},
        {'name': 'cherry', 'color': 'red'},
        {'name': 'date', 'color': 'brown'}
    ]
    sorted_data = sort_dicts_by_key(sample_data)
    print(sorted_data)