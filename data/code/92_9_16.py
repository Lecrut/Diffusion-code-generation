LOGICAL_OPPOSITE = {True: False, False: True}

def print_logical_opposite(boolean_value):
    inverted_value = LOGICAL_OPPOSITE[boolean_value]
    print(inverted_value)
if __name__ == '__main__':
    print_logical_opposite(True)
    print_logical_opposite(False)