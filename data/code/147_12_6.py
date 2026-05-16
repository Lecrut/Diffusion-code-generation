def sort_strings_alphabetically(string_list):
    string_list.sort()
if __name__ == '__main__':
    list1 = ["banana", "apple", "cherry", "date"]
    print("Original list 1:", list1)
    sort_strings_alphabetically(list1)
    print("Sorted list 1:", list1)
    list2 = ["zebra", "ant", "bear", "cat"]
    print("Original list 2:", list2)
    sort_strings_alphabetically(list2)
    print("Sorted list 2:", list2)
    list3 = ["a", "b", "c", "aa", "bb"]
    print("Original list 3:", list3)
    sort_strings_alphabetically(list3)
    print("Sorted list 3:", list3)
    list4 = []
    print("Original list 4:", list4)
    sort_strings_alphabetically(list4)
    print("Sorted list 4:", list4)