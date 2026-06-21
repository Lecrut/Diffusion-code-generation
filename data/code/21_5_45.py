def quicksort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quicksort(arr, low, pi - 1)
        _quicksort(arr, pi + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__':
    sample_values = [4, 2, 5, 1, 3]
    try:
        quicksort(sample_values)
        print(sample_values)
    except ValueError as e:
        print(e)