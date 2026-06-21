def custom_sort(arr):
    if not all(isinstance(x, str) and x.isdigit() for x in arr):
        raise ValueError("All elements must be numeric strings.")
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(arr[j]) > int(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    string_list = ["4", "23", "56", "1", "78"]
    print("Original list:", string_list)
    custom_sort(string_list)
    print("Sorted list:", string_list)