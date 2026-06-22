BOOL_INVERT = {True: False, False: True}

def flip_bool_value(value: bool) -> bool:
    return BOOL_INVERT[value]

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))