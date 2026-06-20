opposite_truth_table = {True: False, False: True}

def opposite_truth(value):
    return opposite_truth_table[value]

if __name__ == '__main__':
    print(opposite_truth(True))
    print(opposite_truth(False))