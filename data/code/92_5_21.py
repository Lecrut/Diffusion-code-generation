OPPOSITE_TRUTH_TABLE = {True: False, False: True}

def opposite_truth(iterable):
    for value in iterable:
        yield OPPOSITE_TRUTH_TABLE[value]
if __name__ == '__main__':
    sample_values = [True, False, True, False]
    for result in opposite_truth(sample_values):
        print(result)