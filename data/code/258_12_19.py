import numpy as np

class PairAverager:
    def get_overall_average(self, data):
        if not data:
            return 0
        pairs = np.array(data)
        valid_pairs = pairs[np.isfinite(pairs[:, 0]) & np.isfinite(pairs[:, 1])]
        if len(valid_pairs) == 0:
            return 0
        total_sum = np.sum(valid_pairs, axis=1)
        count = len(valid_pairs)
        return total_sum.mean()

if __name__ == '__main__':
    averager = PairAverager()
    sample_data = [[1, 2], [3, 4], ['a', 5], [6, 'b'], [7, 8]]
    print(averager.get_overall_average(sample_data))