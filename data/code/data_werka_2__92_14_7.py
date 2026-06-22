def invert_truth(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean")
    table = {True: False, False: True}
    return table[flag]

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))