import numpy as np

def compute_mean(sequence):
    if np:
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(compute_mean(sample_sequence))