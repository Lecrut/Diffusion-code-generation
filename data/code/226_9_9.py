import numpy as np
NUM_REPETITIONS = 3

def repeat_sequence(sequence):
    return np.tile(sequence, (NUM_REPETITIONS, 1))
if __name__ == '__main__':
    sample_array = [0.5, 1.2, 2.8]
    repeated_array = repeat_sequence(sample_array)
    print(repeated_array)