def sort_by_key(data, key):
    sorted_data = {}
    for item in data:
        if key in item:
            value = item[key]
            if value not in sorted_data:
                sorted_data[value] = []
            sorted_data[value].append(item)
    return sorted_data
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 35, 'city': 'Chicago'}
    ]
    key_to_sort = 'city'
    result = sort_by_key(sample_data, key_to_sort)
    print(result)