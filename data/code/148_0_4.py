def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)
if __name__ == '__main__':
    sample_list = [10, 4, 20, 15, 8]
    largest = find_largest(sample_list)
    print(largest)