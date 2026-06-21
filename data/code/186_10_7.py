def validate_input(arr):
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements in the array must be integers")

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    L, R = arr[left:left + len1], arr[mid + 1:mid + 1 + len2]
    i, j, k = 0, 0, left
    while i < len1 and j < len2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = R[j]
        j += 1
        k += 1

def timsort(arr):
    min_run = 32
    n = len(arr)
    validate_input(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min(left + size * 2 - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2
    return arr

if __name__ == '__main__':
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = timsort(unsorted_numbers)
    print(sorted_numbers)