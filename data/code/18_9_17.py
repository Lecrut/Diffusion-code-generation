def get_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) // 2
    return sorted_numbers[mid]

if __name__ == '__main__':
    test_list_1 = [3, 1, 4, 1, 5]
    test_list_2 = [10, 2, 8, 6]
    test_list_3 = [15, 20, 25, 30, 35]
    print(get_median(test_list_1))
    print(get_median(test_list_2))
    print(get_median(test_list_3))