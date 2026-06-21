def reverse_list_of_integers(integer_list):
    if not all(isinstance(i, int) for i in integer_list):
        raise ValueError("All elements in the list must be integers")
    return integer_list[::-1]

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    output = reverse_list_of_integers(input_list)
    print(output)