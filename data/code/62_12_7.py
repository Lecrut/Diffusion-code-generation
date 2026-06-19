def get_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    second_element = get_second_element(my_list)
    print(second_element)

    # Additional test cases
    short_list = [5, 15]
    single_element_list = [7]
    empty_list = []

    print(get_second_element(short_list))        # Should print 15
    print(get_second_element(single_element_list))  # Should print None
    print(get_second_element(empty_list))         # Should print None