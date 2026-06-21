def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect_median(arr, low, high):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if pivot_index == len(arr) // 2:
        return arr[pivot_index]
    elif pivot_index < len(arr) // 2:
        return quickselect_median(arr, pivot_index + 1, high)
    else:
        return quickselect_median(arr, low, pivot_index - 1)

def find_median(data):
    n = len(data)
    if n == 0:
        return None
    return quickselect_median(data, 0, n - 1)

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(find_median(list1))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_median(list2))