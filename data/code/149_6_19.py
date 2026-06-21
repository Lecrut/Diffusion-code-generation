def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    my_list = [5, 4, 3, 2, 1]
    reversed_list = reverse_list(my_list)
    print(reversed_list)