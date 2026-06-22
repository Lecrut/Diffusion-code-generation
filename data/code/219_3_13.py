def find_largest(numbers):
    if not numbers:
        return None
    try:
        return max(numbers)
    except ValueError:
        return "Error: Invalid input detected"

if __name__ == '__main__':
    sample_values = (3, 5, 1, 8, 2)
    result = find_largest(sample_values)
    print(result)