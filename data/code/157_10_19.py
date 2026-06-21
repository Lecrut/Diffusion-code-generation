def find_smallest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return min(numbers)

if __name__ == '__main__':
    sample_list = [34, 12, 56, 9, 88, 23, 10]
    result = find_smallest_value(sample_list)
    print(result)