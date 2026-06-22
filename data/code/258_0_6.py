class PairAverageCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_averages(self):
        sum_first = 0
        sum_second = 0
        count = len(self.data)
        for first, second in self.data:
            sum_first += first
            sum_second += second
        average_first = sum_first / count if count > 0 else 0
        average_second = sum_second / count if count > 0 else 0
        return average_first, average_second

if __name__ == '__main__':
    calculator = PairAverageCalculator([(1, 5), (2, 8), (3, 10), (4, 12)])
    avg_first, avg_second = calculator.calculate_averages()
    print(f"Average of first elements: {avg_first}")
    print(f"Average of second elements: {avg_second}")