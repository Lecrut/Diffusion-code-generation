def sort_numeric_strings(arr):
    return sorted(arr, key=lambda x: int(x))

if __name__ == '__main__':
    string_list = ["10", "5", "20", "3", "7"]
    print("Original list:", string_list)
    sorted_list = sort_numeric_strings(string_list)
    print("Sorted list:", sorted_list)