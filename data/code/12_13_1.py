def get_median_value(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    median_index = length // 2
    return sorted_numbers[median_index]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    result = get_median_value(sample_data)
    print(result)