import numpy as np

MEAN_CALCULATION_THRESHOLD = 1000

def compute_mean(sequence):
    if isinstance(sequence, np.ndarray) and len(sequence) > MEAN_CALCULATION_THRESHOLD:
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [1.5, 2.5, 3.5, 4.5]
    print(compute_mean(sample_sequence))