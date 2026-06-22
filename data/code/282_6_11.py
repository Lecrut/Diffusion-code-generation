import time

class Calculator:
    @staticmethod
    def calculate_total(numbers):
        return sum(numbers)

    @staticmethod
    def measure_execution_time(numbers):
        start_time = time.time()
        total = Calculator.calculate_total(numbers)
        end_time = time.time()
        return total, end_time - start_time

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    total, execution_time = Calculator.measure_execution_time(sample_numbers)
    print(f"Total: {total}")
    print(f"Execution time: {execution_time} seconds")