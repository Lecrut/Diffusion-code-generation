import statistics

class ArithmeticMeanCalculator:
    @staticmethod
    def calculate_mean(values):
        if not values:
            raise ValueError("Input list cannot be empty")
        return statistics.mean(values)

if __name__ == '__main__':
    calculator = ArithmeticMeanCalculator()
    sample_values = [10, 20, 30, 40, 50]
    try:
        mean_value = calculator.calculate_mean(sample_values)
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)