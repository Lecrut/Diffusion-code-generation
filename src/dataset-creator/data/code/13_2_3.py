def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input array is empty.")
    for item in numbers:
        try:
            float(item)
        except (ValueError, TypeError):
            return None
    max_value = float('-inf')
    result = []
    for num in numbers:
        value = float(num)
        if value > max_value or len(result) == 0:
            max_value = value
            result.append(value)
    return int(max_value), result
if __name__ == '__main__':
    sample_array = [3, '5', -1.2, '7']
    try:
        largest_num, all_nums = find_largest_number(sample_array)
        if isinstance(largest_num, float):
            print(f"Error: Non-numeric element detected in input.")
        else:
            print(f"Largest number is {largest_num}")
    except ValueError as e:
        print(e)