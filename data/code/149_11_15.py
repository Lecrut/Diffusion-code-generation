def reverse_list_in_place(data_list):
    if not isinstance(data_list, list) or not all(isinstance(item, str) for item in data_list):
        raise ValueError("Input must be a list of strings")
    
    data_list.reverse()

if __name__ == '__main__':
    my_strings = ["apple", "banana", "cherry"]
    print("Original list:", my_strings)
    reverse_list_in_place(my_strings)
    print("Reversed list:", my_strings)