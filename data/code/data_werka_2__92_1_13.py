class TruthTable:
    OPPOSITE = {True: False, False: True}

    @staticmethod
    def get_opposite(value):
        return TruthTable.OPPOSITE[value]

def find_opposite_truth(value):
    return TruthTable.get_opposite(value)

if __name__ == '__main__':
    true_val = True
    false_val = False
    print(find_opposite_truth(true_val))
    print(find_opposite_truth(false_val))