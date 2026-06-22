def find_median_index(lst):
    if not lst:
        return None
    n = len(lst)
    median_value = lst[n // 2] if n % 2 != 0 else (lst[n // 2 - 1] + lst[n // 2]) / 2
    for i, val in enumerate(lst):
        if val == median_value:
            return i
    return None

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_median_index(sample_list)
    print(result)