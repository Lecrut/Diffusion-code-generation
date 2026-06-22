TRUE_FALSE_MAP = {True: False, False: True}

def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return TRUE_FALSE_MAP[value]

if __name__ == '__main__':
    val1 = find_opposite_truth(True)
    val2 = find_opposite_truth(False)
    print(val1)
    print(val2)