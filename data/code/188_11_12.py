def reverse_list_in_place(lst):
    lst.reverse()

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    print('Original list:', sample_list)
    reverse_list_in_place(sample_list)
    print('Reversed list:', sample_list)