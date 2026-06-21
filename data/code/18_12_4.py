def median_index_value(lst):
    if not lst:
        raise ValueError('List must not be empty')
    n = len(lst)
    indices = list(range(n))

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if lst[arr[j]] <= lst[pivot]:
                i += 1
                arr[i], arr[j] = (arr[j], arr[i])
        arr[i + 1], arr[high] = (arr[high], arr[i + 1])
        return i + 1

    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)
    n = len(lst)
    if n % 2 == 1:
        idx = quickselect(indices, 0, n - 1, n // 2)
        return lst[idx]
    else:
        idx1 = quickselect(indices, 0, n - 1, n // 2 - 1)
        indices2 = list(range(n))
        idx2 = quickselect(indices2, 0, n - 1, n // 2)
        val1 = lst[idx1]
        val2 = lst[idx2]
        return (val1 + val2) / 2
if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9, 2]
    result = median_index_value(sample_list)
    print(result)