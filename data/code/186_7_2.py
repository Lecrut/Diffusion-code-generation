def string_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
if __name__ == '__main__':
    data = ["banana", "apple", "zebra", "grape", "kiwi"]
    print("Original list:", data)
    string_sort(data)
    print("Sorted list:", data)