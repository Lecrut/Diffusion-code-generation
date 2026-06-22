import numpy as np

NUMBERS = [1.5, 2.5, 3.5, 4.5]

def compute_mean(sequence):
    if isinstance(sequence, np.ndarray):
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    print(compute_mean(NUMBERS))