def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = sort_dicts_by_key(data, 'age')
    print(sorted_data)