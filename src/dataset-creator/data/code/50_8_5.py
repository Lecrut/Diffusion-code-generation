from typing import Union
class SumCalculator:
    def calculate_sum(self, a: int, b: int, c: int) -> int:
        return (a + b + c) if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) else None
if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(10, 20, 30)
    print(result)