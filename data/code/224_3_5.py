import numpy as np

def compute_mean(sequence):
    if isinstance(sequence, (list, tuple)) and all(isinstance(x, float) for x in sequence):
        return sum(sequence) / len(sequence)
    elif isinstance(sequence, np.ndarray) and sequence.dtype == np.float64:
        return np.mean(sequence)
    else:
        raise ValueError("Input must be a list or tuple of floats or a numpy array of floats")

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    print(compute_mean(sample_numbers))