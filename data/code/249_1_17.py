def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_list = [15.7, 8.3, 22.4, 4.9, 30.6, 11.2]
    result = find_largest(sample_list)
    print(result)