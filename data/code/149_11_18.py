def reverse_list_in_place(data_list):
    data_list.reverse()

if __name__ == '__main__':
    my_strings = ["hello", "world", "this", "is", "python"]
    print("Original list:", my_strings)
    reverse_list_in_place(my_strings)
    print("Reversed list:", my_strings)