def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid_index = n // 2
    if n % 2 == 1:
        median = sorted_data[mid_index]
    else:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
    return median

if __name__ == '__main__':
    sample_list1 = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]
    print(f"Median of {sample_list1}: {calculate_median(sample_list1)}")
    
    sample_list2 = [1.2, 3.4, 2.1, 5.6, 4.7, 9.8, 8.9, 7.0, 6.1, 5.2]
    print(f"Median of {sample_list2}: {calculate_median(sample_list2)}")