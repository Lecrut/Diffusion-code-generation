TRUE_MAP = {True: False, False: True}

def invert_truth(val):
    return TRUE_MAP[val]

if __name__ == '__main__':
    print(invert_truth(True))
    print(invert_truth(False))