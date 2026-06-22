def is_sorted_ascending(data_list):
    if not all(isinstance(x, (int, float)) for x in data_list):
        raise ValueError("All elements must be numbers.")
    
    return data_list == sorted(data_list)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Sorted in ascending order: {is_sorted_ascending(sample_data)}")
    
    sample_data_desc = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Data: {sample_data_desc}")
    print(f"Sorted in ascending order: {is_sorted_ascending(sample_data_desc)}")
    
    sample_data_mixed = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data_mixed}")
    print(f"Sorted in ascending order: {is_sorted_ascending(sample_data_mixed)}")
    
    sample_data_string = ["apple", "banana", "cherry"]
    try:
        print(f"Data: {sample_data_string}")
        print(f"Sorted in ascending order: {is_sorted_ascending(sample_data_string)}")
    except ValueError as e:
        print(e)