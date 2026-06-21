from operator import itemgetter

def sort_dicts_by_key(data, key):
    return sorted(data, key=itemgetter(key))

if __name__ == '__main__':
    sample_list = [
        {'item': 'apple', 'price': 2.5},
        {'item': 'banana', 'price': 1.0},
        {'item': 'cherry', 'price': 3.75}
    ]
    sorted_list = sort_dicts_by_key(sample_list, 'price')
    print(sorted_list)