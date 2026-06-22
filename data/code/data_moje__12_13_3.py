def get_median_index_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    mid_index = len(sorted_numbers) // 2
    return sorted_numbers[mid_index]

if __name__ == '__main__':
    sample_list = [12, 4, 5, 3, 7, 14, 1]
    result = get_median_index_value(sample_list)
    print(result)