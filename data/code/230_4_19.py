import itertools

class RunningTotalCalculator:
    @staticmethod
    def calculate_running_total(numbers):
        return tuple(itertools.accumulate(numbers))

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    calculator = RunningTotalCalculator()
    result = calculator.calculate_running_total(sample_numbers)
    print(result)