import operator

def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_dicts_1 = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    print("Sample 1:")
    print(sort_dicts_by_key(sample_dicts_1, 'age'))

    sample_dicts_2 = [{'name': 'Charlie', 'score': 85}, {'name': 'David', 'score': 90}]
    print("\nSample 2:")
    print(sort_dicts_by_key(sample_dicts_2, 'score'))

    sample_dicts_3 = [{'name': 'Eve', 'height': 165}, {'name': 'Frank', 'height': 175}]
    print("\nSample 3:")
    print(sort_dicts_by_key(sample_dicts_3, 'height'))