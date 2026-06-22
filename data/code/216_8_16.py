def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 != 0:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    try:
        median_value = calculate_median(sample_list)
        print(f"The median of {sample_list} is {median_value}")
    except ValueError as e:
        print(e)