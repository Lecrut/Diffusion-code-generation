def get_median_index_value(numbers):
    if not numbers:
        return None
    mid = len(numbers) // 2
    return numbers[mid]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_median_index_value(sample_data)
    print(result)