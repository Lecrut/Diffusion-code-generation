def reverse_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    return input_list[::-1]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(my_list)
    print(reversed_list)