import numpy as np

def compute_mean(sequence):
    if isinstance(sequence, np.ndarray):
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(compute_mean(sample_values))