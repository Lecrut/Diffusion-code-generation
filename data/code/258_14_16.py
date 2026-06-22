class AverageCalculator:
    DEFAULT_SAMPLES = [
        (10, 20),
        (30, 40),
        (50, 60),
        ('a', 'b')
    ]

    @staticmethod
    def calculate_averages(pairs):
        sum_first = count_first = 0
        sum_second = count_second = 0

        for a, b in pairs:
            if isinstance(a, (int, float)):
                sum_first += a
                count_first += 1
            if isinstance(b, (int, float)):
                sum_second += b
                count_second += 1

        avg_first = sum_first / count_first if count_first > 0 else 0
        avg_second = sum_second / count_second if count_second > 0 else 0

        return avg_first, avg_second

if __name__ == '__main__':
    calculator = AverageCalculator()
    averages = calculator.calculate_averages(AverageCalculator.DEFAULT_SAMPLES)
    print(f"Averages: {averages}")