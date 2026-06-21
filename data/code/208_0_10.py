import statistics

class MeanCalculator:
    @staticmethod
    def calculate_mean(numbers):
        return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.0]
    calculator = MeanCalculator()
    print(calculator.calculate_mean(sample_values))