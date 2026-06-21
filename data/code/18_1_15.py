def get_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

if __name__ == '__main__':
    even_list = [1, 3, 5, 7]
    odd_list = [1, 3, 5]
    single_list = [10]
    empty_list = []

    print(get_median(even_list))
    print(get_median(odd_list))
    print(get_median(single_list))
    print(get_median(empty_list))