def get_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) // 2
    else:
        return sorted_arr[mid]

if __name__ == '__main__':
    print(get_median([1, 3, 5, 7, 9]))
    print(get_median([4, 2, 8, 6]))
    print(get_median([10, 20]))
    print(get_median([1]))