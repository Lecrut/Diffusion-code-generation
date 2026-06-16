def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input array is empty.")
    for num in numbers:
        try:
            float(num)
        except (TypeError, ValueError):
            raise TypeError(f"Non-numeric element found: {num}")
    return max(float(x) for x in numbers)
if __name__ == '__main__':
    sample_array = [3.5, '10', 7, -2, float('inf')]
    try:
        result = find_largest_number(sample_array)
        print(f"Largest number is: {result}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")