def reverse_iterable(iterable):
    return reversed(list(iterable))
if __name__ == '__main__':
    my_tuple = (1, 2, 3, 4, 5)
    my_string = "hello"
    my_set = {10, 20, 30}
    reversed_tuple = reverse_iterable(my_tuple)
    reversed_string = reverse_iterable(my_string)
    reversed_set = reverse_iterable(my_set)
    print(f"Original tuple: {my_tuple}")
    print(f"Reversed tuple: {reversed_tuple}")
    print(f"Original string: {my_string}")
    print(f"Reversed string: {reversed_string}")
    print(f"Original set: {my_set}")
    print(f"Reversed set (as list): {reversed_set}")