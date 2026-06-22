TRUE_VALUE = True
FALSE_VALUE = False

def flip_bool_value(value: bool) -> bool:
    if value is TRUE_VALUE:
        return FALSE_VALUE
    return TRUE_VALUE

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))