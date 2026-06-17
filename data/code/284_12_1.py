def reverse_iterable(iterable):
    return reversed(iterable)
if __name__ == '__main__':
    my_tuple = (1, 2, 3, 4, 5)
    my_string = "hello"
    my_list = [10, 20, 30]
    reversed_tuple = list(reverse_iterable(my_tuple))
    reversed_string = list(reverse_iterable(my_string))
    reversed_list = list(reverse_iterable(my_list))
    print(f"Original tuple: {my_tuple}")
    print(f"Reversed tuple: {reversed_tuple}")
    print(f"Original string: {my_string}")
    print(f"Reversed string: {reversed_string}")
    print(f"Original list: {my_list}")
    print(f"Reversed list: {reversed_list}")