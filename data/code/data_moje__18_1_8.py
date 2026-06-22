def get_median(sorted_list):
    n = len(sorted_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0

if __name__ == '__main__':
    print(get_median([1, 3, 5]))
    print(get_median([1, 3, 5, 7]))
    print(get_median([10]))
    print(get_median([]))
    print(get_median([2, 4]))