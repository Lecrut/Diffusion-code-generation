def custom_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
if __name__ == '__main__':
    string_list = ["banana", "apple", "zebra", "grape", "date"]
    print("Original list:", string_list)
    custom_sort(string_list)
    print("Sorted list:", string_list)