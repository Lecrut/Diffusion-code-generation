def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input array cannot be empty.")
    for num in numbers:
        try:
            float(num)
        except (ValueError, TypeError):
            raise ValueError(f"Non-numeric element found: {num}")
    return max(float(x) for x in numbers)
if __name__ == '__main__':
    sample_data = [10.5, 23, "4", -7, None]
    try:
        result = find_largest_number(sample_data)
        print(f"Largest number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")