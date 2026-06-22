class PairAverageCalculator:
    def __init__(self):
        self.sum_first = 0
        self.sum_second = 0
        self.count = 0

    def add_pair(self, first, second):
        self.sum_first += first
        self.sum_second += second
        self.count += 1

    def calculate_averages(self):
        if self.count == 0:
            return {"first_average": None, "second_average": None}
        avg_first = self.sum_first / self.count
        avg_second = self.sum_second / self.count
        return {"first_average": avg_first, "second_average": avg_second}

if __name__ == '__main__':
    calculator = PairAverageCalculator()
    calculator.add_pair(10, 20)
    calculator.add_pair(30, 40)
    calculator.add_pair(50, 60)
    result = calculator.calculate_averages()
    print(result)