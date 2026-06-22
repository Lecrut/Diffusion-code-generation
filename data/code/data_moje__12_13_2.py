def get_median_index_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    return sorted_numbers[middle_index]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2]
    result = get_median_index_value(sample_data)
    print(result)