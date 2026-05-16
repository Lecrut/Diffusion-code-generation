def sort_list_of_dicts(data, key):
    return sorted(data, key=lambda x: x[key])
if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 25, 'score': 92},
        {'name': 'Charlie', 'age': 35, 'score': 88},
        {'name': 'David', 'age': 25, 'score': 95}
    ]
    key_to_sort_by = 'age'
    sorted_data = sort_list_of_dicts(data, key_to_sort_by)
    print(sorted_data)