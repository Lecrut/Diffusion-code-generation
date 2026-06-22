def compare_min_max(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists.")
    
    min_val = min(min(list1), min(list2))
    max_val = max(max(list1), max(list2))
    
    return min_val, max_val

if __name__ == '__main__':
    sample_list_1 = [3.14, 1.618, 2.718, 0.577, 9.99]
    sample_list_2 = [-10.5, 5.2, 0.0, 15.8]
    
    min_val, max_val = compare_min_max(sample_list_1, sample_list_2)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")