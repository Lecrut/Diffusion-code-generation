from statistics import mean

class AverageCalculator:
    DEFAULT_SAMPLE = [1.0, 2.0, 3.0, 4.0, 5.0]

    @staticmethod
    def calculate_average(numbers: list) -> float:
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return mean(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    try:
        average = calculator.calculate_average(AverageCalculator.DEFAULT_SAMPLE)
        print(average)
    except ValueError as e:
        print(e)