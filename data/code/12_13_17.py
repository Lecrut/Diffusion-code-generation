def get_median_index_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2
    return sorted_numbers[middle_index]

if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9]
    result = get_median_index_value(sample_list)
    print(result)