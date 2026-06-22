import numpy as np

def mean(sequence):
    if np.array(sequence).dtype == np.float64:
        return np.mean(sequence)
    else:
        return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [1.5, 2.5, 3.5, 4.5]
    print(mean(sample_sequence))