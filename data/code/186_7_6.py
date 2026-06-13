def custom_string_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
if __name__ == '__main__':
    string_list = ["banana", "apple", "zebra", "grape", "mango"]
    print("Original list:", string_list)
    sorted_list = custom_string_sort(string_list)
    print("Sorted list:", sorted_list)