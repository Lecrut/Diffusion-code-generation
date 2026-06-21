def is_valid_numeric_string(s):
    return s.isdigit()

def convert_to_int(s):
    return int(s)

def custom_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    string_list = ["34", "23", "56", "78", "12"]
    print("Original list:", string_list)
    sorted_list = custom_sort(string_list)
    print("Sorted list:", sorted_list)