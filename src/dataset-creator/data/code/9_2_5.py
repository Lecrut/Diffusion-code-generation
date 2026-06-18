class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10.5, 20.5, 30.0, 40.0]
    data2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    data3 = []
    print(calculator.compute_average(data1))
    print(calculator.compute_average(data2))
    print(calculator.compute_average(data3))