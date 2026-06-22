def is_iterable(obj):
    return hasattr(obj, '__iter__') and not isinstance(obj, str)

def calculate_average_of_lists(list_of_lists):
    if not all(is_iterable(lst) for lst in list_of_lists):
        raise ValueError("All elements must be iterable")
    
    total_sum = sum(sum(lst) for lst in list_of_lists)
    total_count = sum(len(lst) for lst in list_of_lists)
    
    if total_count == 0:
        return 0.0
    
    return float(total_sum / total_count)

if __name__ == '__main__':
    sample_data1 = [1, 2, 3]
    sample_data2 = [4, 5]
    sample_data3 = [6, 7, 8, 9]
    
    average_result = calculate_average_of_lists([sample_data1, sample_data2, sample_data3])
    print(average_result)