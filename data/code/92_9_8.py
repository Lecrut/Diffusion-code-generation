def print_logical_opposite(boolean_value: bool) -> None:
    logical_opposites = {True: False, False: True}
    inverted_value = logical_opposites[boolean_value]
    print(inverted_value)

if __name__ == '__main__':
    print_logical_opposite(True)
    print_logical_opposite(False)