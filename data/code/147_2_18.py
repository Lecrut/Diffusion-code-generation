import operator

def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_by_name = sort_dicts_by_key(sample_dicts, 'name')
    print("Sorted by name:")
    for item in sorted_by_name:
        print(item)
    
    sorted_by_age = sort_dicts_by_key(sample_dicts, 'age')
    print("\nSorted by age:")
    for item in sorted_by_age:
        print(item)