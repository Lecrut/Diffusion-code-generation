def reverse_list_inplace(data_list):
    data_list.reverse()
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    reverse_list_inplace(my_list)
    print("Reversed list:", my_list)
    another_list = ['a', 'b', 'c', 'd']
    print("Original list:", another_list)
    reverse_list_inplace(another_list)
    print("Reversed list:", another_list)