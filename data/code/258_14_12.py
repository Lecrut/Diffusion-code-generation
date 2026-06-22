class AverageCalculator:
    DEFAULT_SAMPLE = [
        (10, 20),
        (30, 40),
        (50, 60)
    ]

    @staticmethod
    def calculate_averages(pairs):
        first_elements = [float(pair[0]) for pair in pairs if len(pair) == 2]
        second_elements = [float(pair[1]) for pair in pairs if len(pair) == 2]

        avg_first = sum(first_elements) / len(first_elements) if first_elements else None
        avg_second = sum(second_elements) / len(second_elements) if second_elements else None

        return avg_first, avg_second

if __name__ == '__main__':
    calculator = AverageCalculator()
    avg1, avg2 = calculator.calculate_averages(AverageCalculator.DEFAULT_SAMPLE)
    print(f"Average of the first elements: {avg1}")
    print(f"Average of the second elements: {avg2}")