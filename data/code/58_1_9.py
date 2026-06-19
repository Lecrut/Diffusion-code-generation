def get_first_element(data):
    return data[0] if data else None

if __name__ == '__main__':
    my_list = [7, 14, 21, 28]
    first_element = get_first_element(my_list)
    print(first_element)

    empty_list = []
    first_of_empty = get_first_element(empty_list)
    print(first_of_empty)