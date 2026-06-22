import math

class MeanCalculator:
    DEFAULT_TOLERANCE = 1e-9
    
    @staticmethod
    def calculate_mean(numbers: list) -> float:
        total_sum = math.fsum(numbers)
        count = len(numbers)
        return total_sum / count if count > 0 else 0.0
    
    @staticmethod
    def format_result(value: float) -> str:
        return f"{value:.{2 - int(math.log10(abs(value)))}f}"

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = MeanCalculator()
    mean_value = calculator.calculate_mean(sample_numbers)
    formatted_result = calculator.format_result(mean_value)
    print(formatted_result)