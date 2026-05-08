def reverse_list_in_place(data_list):
    data_list.reverse()
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print(f"Original list: {my_list}")
    reverse_list_in_place(my_list)
    print(f"Reversed list: {my_list}")
    another_list = ['a', 'b', 'c', 'd']
    print(f"Original list: {another_list}")
    reverse_list_in_place(another_list)
    print(f"Reversed list: {another_list}")