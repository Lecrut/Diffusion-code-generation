def find_median(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    try:
        median_value = find_median(sample_data)
        print(median_value)
    except ValueError as e:
        print(e)

    sample_data_even = [1, 2, 3, 4]
    try:
        median_value_even = find_median(sample_data_even)
        print(median_value_even)
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        median_value_empty = find_median(empty_list)
        print(median_value_empty)
    except ValueError as e:
        print(e)