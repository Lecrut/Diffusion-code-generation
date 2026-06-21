class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = AverageCalculator()
    result = calculator.calculate_average(sample_numbers)
    print(f"The calculated average is: {result}")