class AverageCalculator:
    @staticmethod
    def calculate_average(data_iterable):
        if not data_iterable:
            return 0.0
        try:
            total = sum(data_iterable)
            count = len(data_iterable)
            return total / count
        except (TypeError, ZeroDivisionError):
            return 0.0

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [5, 15, 25, 35]
    sample3 = []
    average1 = calculator.calculate_average(sample1)
    print(f"Average of sample1: {average1}")
    average2 = calculator.calculate_average(sample2)
    print(f"Average of sample2: {average2}")
    average3 = calculator.calculate_average(sample3)
    print(f"Average of sample3: {average3}")