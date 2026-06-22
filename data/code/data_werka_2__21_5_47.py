def quicksort(arr):
    def validate_input():
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

    validate_input()
    quicksort_recursive(0, len(arr) - 1)

if __name__ == '__main__':
    sample_values = [4, 2, 5, 1, 3]
    quicksort(sample_values)
    print(sample_values)