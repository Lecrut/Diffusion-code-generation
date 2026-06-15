class StatisticsCalculator:
    def get_average(self, data: list) -> float:
        if not data:
            return 0.0
        total = sum(data)
        count = len(data)
        return total / count
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data = [10, 20, 30, 40, 50]
    average = calculator.get_average(sample_data)
    print(average)