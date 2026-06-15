class PairAverager:
    def get_overall_average(self, data):
        if not data:
            return 0
        total_sum = 0
        count = 0
        for pair in data:
            if isinstance(pair, list) and len(pair) == 2:
                try:
                    total_sum += sum(pair)
                    count += 1
                except TypeError:
                    continue
        if count == 0:
            return 0
        return total_sum / count
if __name__ == '__main__':
    averager = PairAverager()
    sample_data = [
        [10, 20],
        [5, 15],
        [30, 40],
        [2, 8]
    ]
    average = averager.get_overall_average(sample_data)
    print(average)