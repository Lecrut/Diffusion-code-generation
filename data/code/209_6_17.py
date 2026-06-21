class AverageCalculator:
    SAMPLES = [12, 24, 36]

    @staticmethod
    def calculate_average(samples):
        if not samples:
            return 0
        return sum(samples) / len(samples)

if __name__ == '__main__':
    calculator = AverageCalculator()
    average = calculator.calculate_average(AverageCalculator.SAMPLES)
    print(f"The average is: {average}")