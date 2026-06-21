def find_largest_element(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_numbers = [-5, -3, 2, 8, -1]
    result = find_largest_element(sample_numbers)
    print(result)