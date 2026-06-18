import bisect
def optimized_sort_filter(arr: list[int], min_val: int | None = None, max_val: int | None = None) -> list[int]:
    filtered_arr = []
    for item in arr:
        if min_val is not None or max_val is not None:
            if (min_val is None) != (max_val is None):
                lower_bound, upper_bound = min_val, max_val
            else:
                continue
            valid = True
            if min_val is not None and item < min_val:
                valid = False
            if max_val is not None and item > max_val:
                valid = False
        filtered_arr.append(item) if (min_val is None or item >= min_val) else []
    filtered_arr.sort()
    return filtered_arr
if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 5, 6, 3, 7, 4]
    result = optimized_sort_filter(sample_data)
    print(result)