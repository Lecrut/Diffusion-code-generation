def sort_strings_alphabetically(string_list):
    string_list.sort()
if __name__ == '__main__':
    data1 = ["banana", "apple", "cherry", "date"]
    print("Original list 1:", data1)
    sort_strings_alphabetically(data1)
    print("Sorted list 1:", data1)
    data2 = ["zebra", "ant", "bear", "cat"]
    print("Original list 2:", data2)
    sort_strings_alphabetically(data2)
    print("Sorted list 2:", data2)
    data3 = ["a", "b", "c", "a"]
    print("Original list 3:", data3)
    sort_strings_alphabetically(data3)
    print("Sorted list 3:", data3)
    data4 = []
    print("Original list 4:", data4)
    sort_strings_alphabetically(data4)
    print("Sorted list 4:", data4)