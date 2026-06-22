def get_median_index_value(numbers):
    if not numbers:
        return None
    median_index = len(numbers) // 2
    return numbers[median_index]

if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 11]
    result = get_median_index_value(sample_data)
    print(result)