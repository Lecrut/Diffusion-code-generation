def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [42, 15, 89, 3, 77, 6]
    result = find_smallest(sample_values)
    print(result)