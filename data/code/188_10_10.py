def reverse_list_slice(arr):
    return arr[::-1]

if __name__ == '__main__':
    my_list = [8, 7, 6, 5, 4, 3, 2, 1]
    print("Original list:", my_list)
    reversed_list = reverse_list_slice(my_list)
    print("Reversed list:", reversed_list)
    my_list_2 = ['a', 'b', 'c', 'd']
    print("Original list:", my_list_2)
    reversed_list_2 = reverse_list_slice(my_list_2)
    print("Reversed list:", reversed_list_2)