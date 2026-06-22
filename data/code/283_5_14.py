def is_valid_range(value, min_val, max_val):
    return min_val <= value <= max_val

def all_elements_in_range(lst, min_val, max_val):
    if not lst:
        raise ValueError("List cannot be empty")
    if not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
        raise TypeError("Min and max values must be numbers")
    
    return all(is_valid_range(x, min_val, max_val) for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    min_value = 2
    max_value = 10
    print(all_elements_in_range(sample_list, min_value, max_value))