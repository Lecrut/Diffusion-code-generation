def reverse_list_in_place(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list.")
    
    data_list.reverse()

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    reverse_list_in_place(my_list)
    print("Reversed list:", my_list)
    
    another_list = ['a', 'b', 'c', 'd']
    print("Original list:", another_list)
    reverse_list_in_place(another_list)
    print("Reversed list:", another_list)