def get_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) // 2
    return sorted_lst[mid]

if __name__ == '__main__':
    print(get_median([1, 3, 5]))
    print(get_median([1, 2, 3, 4]))
    print(get_median([7, 1, 3]))