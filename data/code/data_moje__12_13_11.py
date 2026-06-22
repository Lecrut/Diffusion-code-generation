def get_median_index_value(numbers):
    if not numbers:
        return None
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_median_index_value(sample_list)
    print(result)