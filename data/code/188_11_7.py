def reverse_list_in_place(lst):
    lst.reverse()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print('Original list:', sample_list)
    reverse_list_in_place(sample_list)
    print('Reversed list:', sample_list)