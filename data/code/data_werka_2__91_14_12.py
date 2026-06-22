TRUE_VALUE = 1
FALSE_VALUE = 0

def flip_bool_value(value: bool) -> bool:
    if value:
        return bool(FALSE_VALUE)
    return bool(TRUE_VALUE)

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))