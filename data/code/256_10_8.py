def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    result = calculate_range(sample_list)
    print(result)
    empty_list = []
    result_empty = calculate_range(empty_list)
    print(result_empty)