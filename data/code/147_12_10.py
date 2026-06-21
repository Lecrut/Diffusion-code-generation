def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    print("Original list 1:", data1)
    sorted_data1 = sort_dicts_by_key(data1, 'age')
    print("Sorted list 1 by age:", sorted_data1)
    
    data2 = [{'name': 'Charlie', 'height': 5.9}, {'name': 'David'}, {'name': 'Eve', 'height': 5.7}]
    print("Original list 2:", data2)
    sorted_data2 = sort_dicts_by_key(data2, 'height')
    print("Sorted list 2 by height:", sorted_data2)
    
    data3 = [{'name': 'Frank'}]
    print("Original list 3:", data3)
    sorted_data3 = sort_dicts_by_key(data3, 'age')
    print("Sorted list 3 by age (default):", sorted_data3)