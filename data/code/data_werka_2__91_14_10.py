def flip_bool_value(value: bool) -> bool:
    if value is True:
        return False
    return True

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))