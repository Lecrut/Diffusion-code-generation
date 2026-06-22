class PairAverages:
    def __init__(self, data):
        self.data = data

    def calculate_averages(self):
        sum_first = 0
        count_first = 0
        sum_second = 0
        count_second = 0
        for pair in self.data:
            if len(pair) >= 2:
                sum_first += pair[0]
                count_first += 1
                sum_second += pair[1]
                count_second += 1
        avg_first = sum_first / count_first if count_first > 0 else 0
        avg_second = sum_second / count_second if count_second > 0 else 0
        return avg_first, avg_second

if __name__ == '__main__':
    sample_data = [
        (10, 5),
        (20, 15)
    ]
    pair_avg_calculator = PairAverages(sample_data)
    avg_first, avg_second = pair_avg_calculator.calculate_averages()
    print(f"Average of first elements: {avg_first}")
    print(f"Average of second elements: {avg_second}")