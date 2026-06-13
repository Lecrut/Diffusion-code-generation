def compare_strings(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if compare_strings(arr1[i], arr2[j]) <= 0:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1
def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
def sort_strings_inplace(arr):
    n = len(arr)
    if n <= 1:
        return
    merge_sort(arr, 0, n - 1)
if __name__ == '__main__':
    string_list = ["banana", "apple", "date", "cherry", "fig", "grape"]
    print("Original list:", string_list)
    sort_strings_inplace(string_list)
    print("Sorted list:", string_list)