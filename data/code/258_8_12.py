class PairAverager:
    def __init__(self):
        self.averages = []

    def add_pair(self, pair):
        if not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, (int, float)) for x in pair):
            raise ValueError("All pairs must contain exactly two numbers.")
        try:
            avg = (pair[0] + pair[1]) / 2
            self.averages.append(avg)
        except TypeError:
            raise ValueError("Error calculating average for a pair.")

    def get_averages(self):
        return tuple(self.averages)

if __name__ == '__main__':
    averager = PairAverager()
    sample_data_valid = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    for pair in sample_data_valid:
        averager.add_pair(pair)
    print(averager.get_averages())