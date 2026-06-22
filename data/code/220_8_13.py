def calculate_average_of_lists(lists):
    if not all(isinstance(lst, list) and isinstance(item, int) for lst in lists for item in lst):
        raise ValueError("All elements must be integers")
    
    total_sum = sum(sum(lst) for lst in lists)
    total_count = sum(len(lst) for lst in lists)
    
    if total_count == 0:
        return 0
    
    return round(total_sum / total_count, 2)

if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    
    average = calculate_average_of_lists([data1, data2, data3])
    print(average)