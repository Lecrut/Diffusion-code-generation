def compare_min_max(list1, list2):
    if not list1:
        min_list1 = None
    else:
        min_list1 = min(list1)
    
    if not list2:
        max_list2 = None
    else:
        max_list2 = max(list2)
    
    return min_list1, max_list2

if __name__ == '__main__':
    sample_data1 = [3.14, 1.618, 2.718, 0.577, 9.99]
    sample_data2 = [-10.5, 5.2, 0.0, 15.8]
    
    min_val1, max_val2 = compare_min_max(sample_data1, sample_data2)
    print(f"Minimum in first list: {min_val1}")
    print(f"Maximum in second list: {max_val2}")