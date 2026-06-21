def find_smallest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return min(numbers)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 7]
    result = find_smallest_value(sample_values)
    print(result)