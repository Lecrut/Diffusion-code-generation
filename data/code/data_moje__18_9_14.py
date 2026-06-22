def get_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 1:
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2

if __name__ == '__main__':
    sample1 = [3, 1, 2]
    sample2 = [4, 1, 3, 2]
    sample3 = [7, 7, 7, 7, 7]

    result1 = get_median(sample1)
    result2 = get_median(sample2)
    result3 = get_median(sample3)

    print(result1)
    print(result2)
    print(result3)