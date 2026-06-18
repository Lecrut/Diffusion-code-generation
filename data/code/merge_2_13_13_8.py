def find_max_value(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("Input list must contain at least one element.")
    max_val = float('-inf')
    for num in numbers:
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            if num > max_val:
                max_val = num
        return max_val
if __name__ == '__main__':
    sample_data = [10.5, 23, -7, 44.9, 8]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found in {sample_data}: {result}")
    except ValueError as e:
        print(f"Error occurred: {e}")