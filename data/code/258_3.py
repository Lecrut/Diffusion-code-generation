class PairAverager:
    def average_all_numbers(self, pairs):
        total_sum = 0
        count = 0
        for pair in pairs:
            if isinstance(pair, list) and len(pair) == 2:
                total_sum += pair[0] + pair[1]
                count += 2
        if count == 0:
            return 0
        return total_sum / count
if __name__ == '__main__':
    averager = PairAverager()
    sample_pairs = [
        [1, 5],
        [10, 20],
        [3, 7]
    ]
    result = averager.average_all_numbers(sample_pairs)
    print(result)