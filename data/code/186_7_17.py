def sort_numeric_strings(lst):
    return sorted(lst, key=lambda x: int(x))

if __name__ == '__main__':
    string_list = ["10", "2", "33", "4"]
    print("Original list:", string_list)
    sorted_list = sort_numeric_strings(string_list)
    print("Sorted list:", sorted_list)