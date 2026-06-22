def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect_median(arr, k):
    if len(arr) % 2 == 1:
        return quickselect(arr, k // 2)
    else:
        return (quickselect(arr, k // 2 - 1) + quickselect(arr, k // 2)) / 2.0

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot_index = partition(arr, 0, len(arr) - 1)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr[:pivot_index], k)
    else:
        return quickselect(arr[pivot_index + 1:], k - pivot_index - 1)

if __name__ == '__main__':
    sample_data = [3, 1, 2, 4, 5]
    print(quickselect_median(sample_data, len(sample_data)))