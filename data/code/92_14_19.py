def invert_truth(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean value")
    truth_map = {True: False, False: True}
    return truth_map[flag]

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))