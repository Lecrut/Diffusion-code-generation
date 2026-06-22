def get_median_via_int_div(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

if __name__ == '__main__':
    arrays = [
        [3, 1, 2],
        [4, 1, 3, 2],
        [10, 20, 30, 40, 50],
        [7],
        [-5, 0, 5, 10, -10, 15]
    ]
    for arr in arrays:
        median_val = get_median_via_int_div(arr)
        print(median_val)