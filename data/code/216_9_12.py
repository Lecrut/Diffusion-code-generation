def calculate_median(data):
    if not data:
        raise ValueError("The input list is empty.")
    
    n = len(data)
    sorted_data = sorted(data)
    
    middle_index = n // 2
    
    if n % 2 == 0:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
    else:
        return sorted_data[middle_index]

if __name__ == '__main__':
    sorted_list_even = [2, 4, 6, 8]
    print(calculate_median(sorted_list_even))
    
    sorted_list_odd = [1, 3, 5, 7, 9]
    print(calculate_median(sorted_list_odd))