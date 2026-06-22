import time

class TotalCalculator:
    @staticmethod
    def calculate_total(numbers):
        return sum(numbers)

    @staticmethod
    def measure_execution_time(func, numbers):
        start_time = time.time()
        result = func(numbers)
        end_time = time.time()
        return result, end_time - start_time

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    calculator = TotalCalculator()
    total, execution_time = calculator.measure_execution_time(TotalCalculator.calculate_total, sample_numbers)
    print(f"Total: {total}")
    print(f"Execution time: {execution_time} seconds")