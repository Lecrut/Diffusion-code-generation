def is_valid_list(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a non-empty list of numbers")

def get_middle_value(data):
    is_valid_list(data)
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Middle value for sample list:", get_middle_value(sample_list))
    
    sample_list_odd = [1, 2, 3, 4, 5]
    print("Middle value for odd length list:", get_middle_value(sample_list_odd))
    
    large_list = list(range(1000000))
    print("Middle value for large list:", get_middle_value(large_list[:10]))