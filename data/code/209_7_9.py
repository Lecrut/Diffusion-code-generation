class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self) -> float:
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data)

if __name__ == '__main__':
    calculator = StatisticsCalculator([7.7, 8.8, 9.9])
    mean_value = calculator.calculate_mean()
    print(mean_value)