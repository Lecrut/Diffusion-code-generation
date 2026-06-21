class TruthTable:
    LOOKUP = {True: False, False: True}

@staticmethod
def find_opposite_truth(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return TruthTable.LOOKUP[value]

if __name__ == '__main__':
    print(find_opposite_truth(True))
    print(find_opposite_truth(False))