def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    my_list = ['a', 'b', 'c', 'd', 'e']
    reversed_list = reverse_list(my_list)
    print(reversed_list)