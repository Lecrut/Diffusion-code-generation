from typing import TypeVar, Union
T = TypeVar('T')
class SumCalculator:
    def __init__(self):
        pass
    @staticmethod
    def calculate_sum(a: T, b: T, c: T) -> T:
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    result_int = calculator.calculate_sum(10, 20, 30)
    print(f"Integer sum: {result_int}")
    result_float = calculator.calculate_sum(5.5, 6.7, 8.9)
    print(f"Float sum: {result_float}")