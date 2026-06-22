class PairAverageCalculator:
    def __init__(self):
        self.data = []

    def add_pair(self, first, second):
        self.data.append((first, second))

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
    calculator = PairAverageCalculator()
    calculator.add_pair(1, 5)
    calculator.add_pair(2, 8)
    calculator.add_pair(3, 10)
    calculator.add_pair(4, 12)
    avg_first, avg_second = calculator.calculate_averages()
    print(f"Average of first elements: {avg_first}")
    print(f"Average of second elements: {avg_second}")