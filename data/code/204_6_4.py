def find_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        middle_index = n // 2
        median = sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2
    return median
if __name__ == '__main__':
    sample_list_odd = [3.5, 1.0, 4.5, 2.0, 3.0]
    sample_list_even = [10.5, 5.5, 20.5, 15.5]
    sample_list_single = [99.9]
    sample_list_empty = []
    print(f"Median of {sample_list_odd}: {find_median(sample_list_odd)}")
    print(f"Median of {sample_list_even}: {find_median(sample_list_even)}")
    print(f"Median of {sample_list_single}: {find_median(sample_list_single)}")
    try:
        find_median(sample_list_empty)
    except ValueError as e:
        print(f"Error for empty list: {e}")