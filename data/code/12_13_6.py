def get_median_index_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_numbers = [1, 3, 2, 5, 4]
    result = get_median_index_value(sample_numbers)
    print(result)