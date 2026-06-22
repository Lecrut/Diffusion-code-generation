import numpy as np
SEQUENCE_UPPER_LIMIT = 25

def generate_sequence():
    return np.arange(1, SEQUENCE_UPPER_LIMIT + 1)
if __name__ == '__main__':
    sequence = generate_sequence()
    print(sequence)