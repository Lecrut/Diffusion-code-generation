def quicksort(arr):
    def validate_input(arr):
        if not isinstance(arr, list):
            raise ValueError("Input must be a list.")
        for x in arr:
            if not isinstance(x, int):
                raise ValueError("All elements in the array must be integers.")

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    validate_input(arr)
    quicksort_recursive(0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 2, 7, 1, 10]
    sorted_values = quicksort(sample_values)
    print(sorted_values)