class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    print(calculator.calculate_average([10, 20, 30, 40, 50]))