def find_max_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_data_1 = [3, 5, -2, 9, 4.7]
    sample_data_2 = [-10, -7, -4, -8]
    result_a = find_max_value(sample_data_1)
    print(f"Maximum of {sample_data_1}: {result_a}")
    result_b = find_max_value(sample_data_2)
    print(f"Maximum of {sample_data_2}: {result_b}")