def sort_numeric_strings(string_list):
    return sorted(string_list, key=lambda x: int(x))

if __name__ == '__main__':
    string_list = ["10", "3", "20", "5", "7"]
    print("Original list:", string_list)
    sorted_list = sort_numeric_strings(string_list)
    print("Sorted list by integer value:", sorted_list)