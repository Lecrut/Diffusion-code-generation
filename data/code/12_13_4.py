def get_median_index_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = get_median_index_value(sample_values)
    print(result)