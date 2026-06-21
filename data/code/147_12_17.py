def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("All elements must be dictionaries")
    return sorted(dict_list, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    data1 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
    print("Original list 1:", data1)
    sorted_data1 = sort_dicts_by_key(data1, 'age')
    print("Sorted list 1 by age:", sorted_data1)

    data2 = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}, {'name': 'Charlie', 'score': 75}]
    print("\nOriginal list 2:", data2)
    sorted_data2 = sort_dicts_by_key(data2, 'score')
    print("Sorted list 2 by score:", sorted_data2)

    data3 = [{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}]
    print("\nOriginal list 3:", data3)
    sorted_data3 = sort_dicts_by_key(data3, 'age')
    print("Sorted list 3 by age (missing key):", sorted_data3)

    data4 = []
    print("\nOriginal list 4 (Empty):", data4)
    sorted_data4 = sort_dicts_by_key(data4, 'name')
    print("Sorted list 4:", sorted_data4)