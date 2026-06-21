def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) // 2
    return sorted_lst[mid]

if __name__ == '__main__':
    samples = [
        [3, 1, 2],
        [4, 1, 3, 2],
        [1],
        [5, 10],
        [7, 7, 7]
    ]
    for arr in samples:
        print(median(arr))