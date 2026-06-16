def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input array is empty.")
    for item in numbers:
        try:
            float(item)
        except (ValueError, TypeError):
            return None
    max_value = -float('inf')
    for num in numbers:
        value = float(num)
        if value > max_value:
            max_value = value
    return int(max_value)
if __name__ == '__main__':
    sample_array = [10, 25.3, "4", -7]
    try:
        result = find_largest_number(sample_array)
        print(f"Largest number: {result}")
    except ValueError as e:
        if str(e).startswith("Input array"):
            print(f"Error: Input is invalid or empty.")
        else:
            raise