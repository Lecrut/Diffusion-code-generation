import statistics

class AverageCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        return statistics.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator([10, 20, 30, 40, 50])
    average = calculator.calculate_average()
    print(average)