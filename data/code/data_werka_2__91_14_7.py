def flip_bool_value(value: bool) -> bool:
    return value ^ True

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))