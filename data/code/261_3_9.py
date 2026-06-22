def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, k):
    low, high = 0, len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

def find_median(lst):
    n = len(lst)
    if n % 2 == 1:
        return quickselect(lst, n // 2)
    else:
        return (quickselect(lst, n // 2 - 1) + quickselect(lst, n // 2)) / 2.0

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_data))