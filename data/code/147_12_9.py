def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(item, dict) for item in dict_list):
        raise ValueError("All elements in the list must be dictionaries.")
    
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    print("Original list 1:", data1)
    sorted_data1 = sort_dicts_by_key(data1, 'age')
    print("Sorted list 1 by age:", sorted_data1)

    data2 = [{'name': 'Charlie', 'score': 85}, {'name': 'David', 'score': 90}]
    print("\nOriginal list 2:", data2)
    sorted_data2 = sort_dicts_by_key(data2, 'score')
    print("Sorted list 2 by score:", sorted_data2)

    data3 = [{'name': 'Eve'}, {'name': 'Frank', 'age': 40}]
    print("\nOriginal list 3:", data3)
    sorted_data3 = sort_dicts_by_key(data3, 'age')
    print("Sorted list 3 by age (missing key handled):", sorted_data3)

    empty_list = []
    print("\nEmpty list:", empty_list)
    try:
        sorted_empty_list = sort_dicts_by_key(empty_list, 'name')
    except ValueError as e:
        print("Error:", e)