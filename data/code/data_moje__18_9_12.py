def get_median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) // 2
    return sorted_numbers[mid_index]

if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5]
    sample_list_2 = [10, 20, 30, 40]
    sample_list_3 = [7]
    print(get_median(sample_list_1))
    print(get_median(sample_list_2))
    print(get_median(sample_list_3))