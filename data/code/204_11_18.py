def find_median(data):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_select(arr, low, high, k):
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quick_select(arr, low, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, high, k)

    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return quick_select(data, 0, n - 1, mid)
    else:
        return (quick_select(data, 0, n - 1, mid - 1) + quick_select(data, 0, n - 1, mid)) / 2.0

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    median_value = find_median(sample_list)
    print(median_value)