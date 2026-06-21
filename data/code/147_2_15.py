from operator import itemgetter

def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_by_age = sort_dicts_by_key(sample_dicts, 'age')
    print("Sorted by age:", sorted_by_age)