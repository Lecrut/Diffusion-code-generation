def get_median_index_value(numbers):
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = get_median_index_value(sample_numbers)
    print(result)