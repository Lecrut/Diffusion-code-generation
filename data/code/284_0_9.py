def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    my_list = [5, 4, 3, 2, 1]
    reversed_list = reverse_list(my_list)
    print(reversed_list)