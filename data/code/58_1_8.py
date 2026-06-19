def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        return None

if __name__ == '__main__':
    my_list = [5, 15, 25, 35]
    first = get_first_element(my_list)
    print(first)

    empty_list = []
    first_empty = get_first_element(empty_list)
    print(first_empty)