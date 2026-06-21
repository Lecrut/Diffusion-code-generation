def get_median_index_value(numbers):
    if not numbers:
        return None
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_data = [10, 23, 45, 67, 89]
    result = get_median_index_value(sample_data)
    print(result)