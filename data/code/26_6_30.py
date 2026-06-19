def filter_by_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    return [x for x in lst if x > median]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = filter_by_median(sample_list)
    print(result)