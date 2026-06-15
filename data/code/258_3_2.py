class PairAverager:
    def average_all(self, pairs):
        total_sum = 0
        pair_count = 0
        for pair in pairs:
            if isinstance(pair, list) and len(pair) == 2:
                total_sum += pair[0] + pair[1]
                pair_count += 1
        if pair_count == 0:
            return 0
        else:
            return total_sum / pair_count
if __name__ == '__main__':
    averager = PairAverager()
    sample_pairs = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    result = averager.average_all(sample_pairs)
    print(result)