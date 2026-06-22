def invert_truth(val):
    if not isinstance(val, bool):
        raise ValueError("Expected boolean input")
    table = {True: False, False: True}
    return table[val]

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))