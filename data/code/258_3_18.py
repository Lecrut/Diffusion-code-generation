import numpy as np

class PairAverager:
    @staticmethod
    def calculate_average(pair):
        if isinstance(pair, list) and len(pair) == 2:
            return (pair[0] + pair[1]) / 2
        return None

    def average_all_numbers(self, pairs):
        valid_pairs = [self.calculate_average(pair) for pair in pairs if self.calculate_average(pair) is not None]
        if not valid_pairs:
            return np.array([0])
        return np.array(valid_pairs)

if __name__ == '__main__':
    averager = PairAverager()
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7]
    ]
    print(averager.average_all_numbers(sample_pairs))