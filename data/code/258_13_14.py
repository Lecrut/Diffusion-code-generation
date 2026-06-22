class PairAverager:
    def __init__(self, tuple1, tuple2):
        self.tuple1 = tuple1
        self.tuple2 = tuple2

    def average_pairs(self):
        return tuple((a + b) / 2 for a, b in zip(self.tuple1, self.tuple2))

if __name__ == '__main__':
    averager = PairAverager((10, 20, 30), (40, 50, 60))
    result = averager.average_pairs()
    print(result)