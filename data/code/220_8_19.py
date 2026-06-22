def calculate_average_of_int_lists(list_of_lists):
    if not all(isinstance(lst, (list, tuple)) and all(isinstance(item, int) for item in lst) for lst in list_of_lists):
        raise ValueError("Input must be a list of integer lists.")
    
    total_sum = sum(sum(lst) for lst in list_of_lists)
    total_count = sum(len(lst) for lst in list_of_lists)
    
    if total_count == 0:
        return 0.0
    
    average = total_sum / total_count
    return round(average, 2)

if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    lists_to_average = [data1, data2, data3]
    average = calculate_average_of_int_lists(lists_to_average)
    print(average)