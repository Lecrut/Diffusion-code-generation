def get_third_value(data_tuple):
    if not data_tuple:
        raise IndexError("Tuple is empty")
    if len(data_tuple) < 3:
        raise IndexError("Tuple does not have a third element")
    return data_tuple[2]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_third_value(sample_tuple)
    print(result)

    empty_tuple = ()
    try:
        get_third_value(empty_tuple)
    except IndexError as e:
        print(str(e))

    short_tuple = (1, 2)
    try:
        get_third_value(short_tuple)
    except IndexError as e:
        print(str(e))