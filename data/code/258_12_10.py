import numpy as np

class PairAverager:

    def get_overall_average(self, data):
        if not data:
            return 0
        pairs = np.array(data)
        valid_pairs = pairs[np.all(np.isfinite(pairs), axis=1)]
        flattened = valid_pairs.flatten()
        total_sum = np.sum(flattened)
        count = len(flattened)
        if count == 0:
            return 0
        return total_sum / count
if __name__ == '__main__':
    averager = PairAverager()
    sample_data = [[1, 2], [3, 4], [5, np.inf], [np.nan, 6]]
    average = averager.get_overall_average(sample_data)
    print(average)