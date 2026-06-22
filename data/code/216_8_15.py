def calculate_median(lst):
    if not lst:
        raise ValueError('List is empty')
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0
    else:
        return sorted_lst[mid]
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print(calculate_median(sample_list))