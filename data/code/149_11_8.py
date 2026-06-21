def reverse_list_in_place(data_list):
    data_list.reverse()

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    reverse_list_in_place(my_list)
    print("Reversed list:", my_list)

    sample_strings = ["hello", "world"]
    print("Original list:", sample_strings)
    reverse_list_in_place(sample_strings)
    print("Reversed list:", sample_strings)