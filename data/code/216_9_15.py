def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError('The data list cannot be empty')
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 == 1:
        return float(sorted_data[middle_index])
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2.0
if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5, 9, 2]
    print(calculate_median(sample_list_odd))
    sample_list_even = [3, 1, 4, 1, 5, 9, 2, 6]
    print(calculate_median(sample_list_even))