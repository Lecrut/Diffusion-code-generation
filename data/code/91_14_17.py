def flip_bool_value(value: bool) -> bool:
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))