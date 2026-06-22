def get_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) // 2
    return sorted_numbers[mid_index]

if __name__ == '__main__':
    test_data_1 = [10, 5, 3, 8, 2]
    test_data_2 = [1, 2, 3, 4]
    print(get_median(test_data_1))
    print(get_median(test_data_2))