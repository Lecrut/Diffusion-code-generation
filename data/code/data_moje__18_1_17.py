def get_median_sorted_list(sorted_list):
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    test_list_odd = [1, 3, 5, 7, 9]
    test_list_even = [2, 4, 6, 8]
    test_list_single = [42]
    test_list_two = [10, 20]

    print(get_median_sorted_list(test_list_odd))
    print(get_median_sorted_list(test_list_even))
    print(get_median_sorted_list(test_list_single))
    print(get_median_sorted_list(test_list_two))