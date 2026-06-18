def sort_by_key(data, key):
    result = {}
    for item in data:
        if key in item:
            value = item[key]
            if value not in result:
                result[value] = []
            result[value].append(item)
    return result
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 35, 'city': 'Chicago'}
    ]
    key_to_sort = 'city'
    sorted_data_by_city = sort_by_key(sample_data, key_to_sort)
    print(sorted_data_by_city)