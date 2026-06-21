def sort_dicts_by_key(dict_list, key):
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    print("Original list 1:", data1)
    sorted_data1 = sort_dicts_by_key(data1, 'age')
    print("Sorted list 1 by age:", sorted_data1)
    
    data2 = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}]
    print("\nOriginal list 2:", data2)
    sorted_data2 = sort_dicts_by_key(data2, 'score')
    print("Sorted list 2 by score:", sorted_data2)
    
    data3 = [{'name': 'Alice'}, {'name': 'Bob', 'age': 30}]
    print("\nOriginal list 3:", data3)
    sorted_data3 = sort_dicts_by_key(data3, 'age')
    print("Sorted list 3 by age (missing key):", sorted_data3)