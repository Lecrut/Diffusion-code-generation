def validate_input(arr):
    if not all(isinstance(item, str) and item.isdigit() for item in arr):
        raise ValueError("All elements in the list must be numeric strings.")

def custom_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(arr[j]) > int(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    string_list = ["3", "1", "4", "1", "5"]
    validate_input(string_list)
    print("Original list:", string_list)
    custom_sort(string_list)
    print("Sorted list:", string_list)