import numpy as np

class MeanCalculator:
    def __init__(self, data_sequence):
        self.data_sequence = data_sequence
        self._array = None

    def _ensure_array(self):
        if self._array is None:
            self._array = np.asarray(self.data_sequence, dtype=float)

    def get_mean(self):
        self._ensure_array()
        return float(np.mean(self._array))

    def get_sum(self):
        self._ensure_array()
        return float(np.sum(self._array))

    def get_count(self):
        return len(self.data_sequence)

if __name__ == '__main__':
    sample_values = [15.5, 22.1, 18.9, 30.4, 25.0, 12.2, 27.8]
    calculator = MeanCalculator(sample_values)
    print(calculator.get_mean())
    print(calculator.get_sum())
    print(calculator.get_count())