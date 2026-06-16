def find_max_value(numbers):
    if not numbers or all(not isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a non-empty list of numeric values.")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_data_1 = [3, 5, -2, 8.7, 4]
    sample_data_2 = [-10, -40, -8, -99]
    result_1 = find_max_value(sample_data_1)
    print(f"Maximum of {sample_data_1}: {result_1}")
    result_2 = find_max_value(sample_data_2)
    print(f"Maximum of {sample_data_2}: {result_2}")