def get_median_index_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    sorted_numbers = sorted(numbers)
    median_index = len(sorted_numbers) // 2
    return sorted_numbers[median_index]

if __name__ == '__main__':
    sample_list = [7, 1, 3, 9, 2]
    result = get_median_index_value(sample_list)
    print(result)