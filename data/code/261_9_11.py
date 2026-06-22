def calculate_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid_index]
    else:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
if __name__ == '__main__':
    sample_data_odd = [3, 1, 4, 1, 5, 9, 2]
    median_value_odd = calculate_median(sample_data_odd)
    print(median_value_odd)
    sample_data_even = [3, 1, 4, 1, 5, 9, 2, 6]
    median_value_even = calculate_median(sample_data_even)
    print(median_value_even)
    empty_list = []
    median_value_empty = calculate_median(empty_list)
    print(median_value_empty)