import numpy as np

class PairAverager:
    def average_pairs(self, pairs):
        valid_pairs = [pair for pair in pairs if isinstance(pair, list) and len(pair) == 2]
        total_sum = sum(sum(pair) for pair in valid_pairs)
        count = len(valid_pairs) * 2
        return np.array([total_sum / count]) if count > 0 else np.array([0])

if __name__ == '__main__':
    averager = PairAverager()
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7],
        [8, 12]
    ]
    result = averager.average_pairs(sample_pairs)
    print(result)