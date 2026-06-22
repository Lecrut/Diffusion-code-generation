TRUE_FALSE_MAP = {True: False, False: True}

def flip_bool_value(value: bool) -> bool:
    return TRUE_FALSE_MAP[value]

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))