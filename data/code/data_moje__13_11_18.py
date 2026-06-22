def get_element_from_tuple(data_tuple, position):
    try:
        if position < 0:
            position = len(data_tuple) + position
        if 0 <= position < len(data_tuple):
            return data_tuple[position]
        else:
            return None
    except TypeError:
        return None
    except IndexError:
        return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    index = 2
    result = get_element_from_tuple(sample_tuple, index)
    print(result)