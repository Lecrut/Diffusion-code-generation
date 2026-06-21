def timsort(arr):
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min(left + size * 2 - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    len1, len2 = (m - l + 1, r - m)
    left, right = ([], [])
    for i in range(0, len1):
        left.append(arr[l + i])
    for j in range(0, len2):
        right.append(arr[m + 1 + j])
    i, j, k = (0, 0, l)
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1
if __name__ == '__main__':
    sample_array = [34, 8, 64, 51, 32, 21, 90, 76]
    timsort(sample_array)
    print(sample_array)