def get_tuple_element(tup, index):
    try:
        return tup[index]
    except IndexError:
        return None

if __name__ == '__main__':
    my_tuple = (10, 20, 30, 40, 50)
    valid_index = 2
    invalid_index = 10
    print(get_tuple_element(my_tuple, valid_index))
    print(get_tuple_element(my_tuple, invalid_index))