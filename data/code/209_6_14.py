class AverageCalculator:
    SAMPLE_VALUES = [12, 24, 36]

    @staticmethod
    def calculate_average(samples):
        return sum(samples) / len(samples)

if __name__ == '__main__':
    calculator = AverageCalculator()
    average = calculator.calculate_average(AverageCalculator.SAMPLE_VALUES)
    print(f"The average is: {average}")