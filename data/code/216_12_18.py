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
        return quickselect(arr, len(arr) // 2, 0, len(arr) - 1)
    else:
        return (quickselect(arr, len(arr) // 2 - 1, 0, len(arr) - 1) +
                quickselect(arr, len(arr) // 2, 0, len(arr) - 1)) / 2

def quickselect(arr, k, low, high):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, k, low, pivot_index - 1)
    else:
        return quickselect(arr, k, pivot_index + 1, high)

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    median = quickselect_median(data, len(data) // 2)
    print(median)