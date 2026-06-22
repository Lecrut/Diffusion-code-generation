import time

class SumCalculator:
    @staticmethod
    def calculate_total(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    start_time = time.time()
    total = SumCalculator.calculate_total(sample_numbers)
    end_time = time.time()
    print(f"Total: {total}")
    print(f"Execution time: {end_time - start_time} seconds")