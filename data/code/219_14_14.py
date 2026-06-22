def find_largest(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_data = [15, 8, 42, 3, 99, 27, 50]
    result = find_largest(sample_data)
    print(result)