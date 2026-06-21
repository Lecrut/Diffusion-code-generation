def find_smallest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [45, 23, 78, 1, 90, -3, 2]
    result = find_smallest_value(sample_values)
    print(result)