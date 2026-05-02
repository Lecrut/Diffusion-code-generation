def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def sort_list(arr):
    if not arr:
        return arr
    quicksort(arr, 0, len(arr) - 1)
    return arr
if __name__ == '__main__':
    data = [10, 7, 8, 9, 1, 5]
    sorted_data = sort_list(data)
    print(sorted_data)