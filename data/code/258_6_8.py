class PairAverager:
    def __init__(self, pairs):
        self.pairs = pairs

    def calculate_averages(self):
        sum_firsts = 0
        sum_seconds = 0
        count = len(self.pairs)
        for first, second in self.pairs:
            sum_firsts += first
            sum_seconds += second
        average_firsts = sum_firsts / count if count > 0 else 0
        average_seconds = sum_seconds / count if count > 0 else 0
        return {'average_firsts': average_firsts, 'average_seconds': average_seconds}

if __name__ == '__main__':
    pairs_instance = PairAverager([
        (10, 20),
        (5, 15),
        (8, 2),
        (12, 30)
    ])
    result = pairs_instance.calculate_averages()
    print(result)