import numpy as np
REPEAT_COUNT = 3

def repeat_sequence(sequence):
    return np.tile(sequence, (REPEAT_COUNT, 1))
if __name__ == '__main__':
    sample_sequence = np.array([0.1, 0.2, 0.3])
    repeated_sequence = repeat_sequence(sample_sequence)
    print(repeated_sequence)