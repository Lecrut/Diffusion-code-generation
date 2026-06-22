class AverageCalculator:
    EPSILON = 1e-9

    @staticmethod
    def calculate_average(values):
        if not values:
            return 0.0

        total_sum = sum(values)
        count = len(values)

        if abs(total_sum) < AverageCalculator.EPSILON and abs(count) < AverageCalculator.EPSILON:
            return 0.0

        return float(total_sum / count)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = [85, 92, 78, 88]
    average = calculator.calculate_average(sample_values)
    print(average)