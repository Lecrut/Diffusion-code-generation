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
    try:
        result_str = calculator.calculate_sum("hello", "world", "!")
        print(f"String concatenation: '{result_str}'")
    except TypeError as e:
        print(f"Type error occurred: {e}")