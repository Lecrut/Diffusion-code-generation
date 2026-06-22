def is_sorted_ascending(data_list):
    if not all(isinstance(x, (int, float)) for x in data_list):
        raise ValueError("All elements must be numbers.")
    
    return all(data_list[i] <= data_list[i + 1] for i in range(len(data_list) - 1))

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Sorted (ascending): {is_sorted_ascending(sample_data)}")
    
    sample_data_strings = ["apple", "banana", "cherry"]
    try:
        print(f"Data (strings): {sample_data_strings}")
        print(f"Sorted (ascending): {is_sorted_ascending(sample_data_strings)}")
    except ValueError as e:
        print(e)