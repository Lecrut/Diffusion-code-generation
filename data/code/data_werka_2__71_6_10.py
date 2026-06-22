def find_median(lst):
    if not lst:
        raise ValueError("List must not be empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = (n - 1) // 2
    return sorted_lst[mid]

if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9, 2]
    result = find_median(sample_list)
    print(result)