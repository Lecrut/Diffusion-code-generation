def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")

def calculate_median(data):
    validate_input(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle_index = n // 2
    if n % 2 == 0:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
    else:
        return sorted_data[middle_index]

if __name__ == '__main__':
    sample_list_even = [3, 1, 4, 1, 5, 9]
    median_value_even = calculate_median(sample_list_even)
    print(median_value_even)

    sample_list_odd = [2, 7, 1, 8, 2, 8, 5]
    median_value_odd = calculate_median(sample_list_odd)
    print(median_value_odd)