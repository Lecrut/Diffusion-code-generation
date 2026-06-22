import numpy as np

class MeanCalculator:
    @staticmethod
    def compute_mean(sequence):
        if isinstance(sequence, np.ndarray) and sequence.dtype == np.float64:
            return np.mean(sequence)
        else:
            return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    calculator = MeanCalculator()
    print(calculator.compute_mean(sample_numbers))