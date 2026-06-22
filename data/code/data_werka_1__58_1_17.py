def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        return None

if __name__ == '__main__':
    my_list = [7, 14, 21, 28]
    first_element = get_first_element(my_list)
    print(f"The first element of the list is: {first_element}")

    empty_list = []
    first_element_of_empty = get_first_element(empty_list)
    print(f"The first element of an empty list is: {first_element_of_empty}")