def get_median(lst):
    if not lst:
        raise ValueError("List must not be empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid_idx = n // 2
    if n % 2 == 1:
        return sorted_lst[mid_idx]
    else:
        lower = sorted_lst[mid_idx - 1]
        upper = sorted_lst[mid_idx]
        return (lower + upper) // 2

if __name__ == '__main__':
    print(get_median([1, 3, 5, 7, 9]))
    print(get_median([1, 2, 3, 4]))
    print(get_median([10]))
    print(get_median([4, 8, 1, 9, 3, 7]))