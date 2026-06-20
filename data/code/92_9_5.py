def print_logical_opposite(boolean_value: bool) -> None:
    if not isinstance(boolean_value, bool):
        raise ValueError('Input must be a boolean value')
    inverted_value = ~boolean_value & 1
    print(bool(inverted_value))
if __name__ == '__main__':
    try:
        print_logical_opposite(True)
        print_logical_opposite(False)
        print_logical_opposite(1)
    except ValueError as e:
        print(e)