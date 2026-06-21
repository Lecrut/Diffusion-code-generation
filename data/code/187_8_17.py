def find_largest_element(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_numbers = [-5, -3, 10, 2, 7]
    print(find_largest_element(sample_numbers))