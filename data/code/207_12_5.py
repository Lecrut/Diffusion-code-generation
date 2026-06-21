def find_largest(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    result = find_largest(sample_numbers)
    print(result)
    empty_list = []
    result_empty = find_largest(empty_list)
    print(result_empty)