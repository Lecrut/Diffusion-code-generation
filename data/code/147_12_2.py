def sort_strings_alphabetically(string_list):
    string_list.sort()
if __name__ == '__main__':
    sample_list_1 = ["banana", "apple", "cherry", "date"]
    print("Original List 1:", sample_list_1)
    sort_strings_alphabetically(sample_list_1)
    print("Sorted List 1:", sample_list_1)
    sample_list_2 = ["zebra", "yak", "ant", "bear"]
    print("\nOriginal List 2:", sample_list_2)
    sort_strings_alphabetically(sample_list_2)
    print("Sorted List 2:", sample_list_2)
    sample_list_3 = ["a", "b", "c", "d"]
    print("\nOriginal List 3:", sample_list_3)
    sort_strings_alphabetically(sample_list_3)
    print("Sorted List 3:", sample_list_3)
    sample_list_4 = []
    print("\nOriginal List 4 (Empty):", sample_list_4)
    sort_strings_alphabetically(sample_list_4)
    print("Sorted List 4:", sample_list_4)