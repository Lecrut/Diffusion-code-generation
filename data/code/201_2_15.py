class AverageCalculator:
    @staticmethod
    def compute_average(*args):
        if not args:
            return 0.0
        return float(sum(args) / len(args))

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data = [10, 20, 30, 40, 50]
    average = calculator.compute_average(*sample_data)
    print(average)