import numpy as np

class PairAverager:
    def get_overall_average(self, data):
        if not data:
            return 0
        pairs = np.array(data)
        valid_pairs = pairs[np.all(np.isfinite(pairs), axis=1)]
        if len(valid_pairs) == 0:
            return 0
        total_sum = np.sum(valid_pairs)
        count = len(valid_pairs) * 2
        return total_sum / count

if __name__ == '__main__':
    averager = PairAverager()
    sample_data = [[1, 2], [3, 4], [5, None], [6, 7]]
    print(averager.get_overall_average(sample_data))