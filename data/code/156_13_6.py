class StatisticsCalculator:
    def __init__(self, values):
        self.values = values

    @staticmethod
    def calculate_average(nums):
        return sum(nums) / len(nums) if nums else 0

if __name__ == '__main__':
    calculator = StatisticsCalculator([1.5, 2.5, 3.5])
    print(calculator.calculate_average(calculator.values))