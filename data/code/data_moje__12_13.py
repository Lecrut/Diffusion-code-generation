def get_median_index_value(numbers):
    n = len(numbers)
    if n == 0:
        raise ValueError("List cannot be empty")
    if n % 2 == 1:
        middle_index = n // 2
        return numbers[middle_index]
    else:
        middle_index = n // 2
        return numbers[middle_index]

if __name__ == '__main__':
    sample_data = [3, 5, 1, 9, 2, 8, 4]
    result = get_median_index_value(sample_data)
    print(result)