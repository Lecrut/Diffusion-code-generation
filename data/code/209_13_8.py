class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count if count > 0 else 0

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values1 = [10, 20, 30, 40, 50]
    print(calculator.calculate_average(sample_values1))
    
    sample_values2 = [15.5, 25.5, 35.5, 45.5, 55.5]
    print(calculator.calculate_average(sample_values2))