def compare_strings(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare_strings(arr[j], key) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
if __name__ == '__main__':
    data = ["banana", "apple", "cherry", "date", "elderberry"]
    print("Original list:", data)
    insertion_sort(data)
    print("Sorted list:", data)