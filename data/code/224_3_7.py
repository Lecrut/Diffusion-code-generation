import numpy as np

def is_valid_sequence(sequence):
    if not isinstance(sequence, (list, tuple, np.ndarray)):
        raise ValueError("Input must be a list, tuple, or numpy array")
    if not all(isinstance(x, float) for x in sequence):
        raise ValueError("All elements of the input must be floating-point numbers")

def compute_mean(sequence):
    is_valid_sequence(sequence)
    if isinstance(sequence, np.ndarray):
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    print(compute_mean(sample_numbers))