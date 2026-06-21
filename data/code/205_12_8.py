def sort_dict_list_by_key(data, key):
    return sorted(data, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    print("Original data:", sample_data)
    sorted_data = sort_dict_list_by_key(sample_data, 'age')
    print("Sorted by age (descending):", sorted_data)