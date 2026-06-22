def quicksort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements of the list must be integers")

    def _quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            _quicksort(low, pi - 1)
            _quicksort(pi + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quicksort(0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    sample_values = [9, 3, 6, 8, 2, 5, 1, 4, 7]
    sorted_values = quicksort(sample_values)
    print(sorted_values)