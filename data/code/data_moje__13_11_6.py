def get_from_tuple(t, position):
    try:
        return t[position]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    valid_index = 2
    invalid_index = 10

    result_valid = get_from_tuple(sample_tuple, valid_index)
    print(result_valid)

    result_invalid = get_from_tuple(sample_tuple, invalid_index)
    print(result_invalid)