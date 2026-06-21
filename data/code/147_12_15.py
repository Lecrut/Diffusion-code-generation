def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("All elements must be dictionaries")
    if not isinstance(key, str):
        raise ValueError("Key must be a string")

    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    print("Original list 1:", data1)
    sorted_data1 = sort_dicts_by_key(data1, 'age')
    print("Sorted list 1 by age:", sorted_data1)

    data2 = [{'name': 'Alice'}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie'}]
    print("\nOriginal list 2:", data2)
    sorted_data2 = sort_dicts_by_key(data2, 'age')
    print("Sorted list 2 by age (missing values handled):", sorted_data2)

    data3 = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
    print("\nOriginal list 3:", data3)
    sorted_data3 = sort_dicts_by_key(data3, 'age')
    print("Sorted list 3 by age:", sorted_data3)

    data4 = []
    print("\nOriginal list 4 (Empty):", data4)
    sorted_data4 = sort_dicts_by_key(data4, 'age')
    print("Sorted list 4 by age (empty list):", sorted_data4)