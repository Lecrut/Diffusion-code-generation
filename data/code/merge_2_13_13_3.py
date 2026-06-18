def find_max_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return max(numbers)
if __name__ == '__main__':
    sample_data = [10, 25, -3, 42, 7]
    result = find_max_value(sample_data)
    print(f"Maximum value: {result}")