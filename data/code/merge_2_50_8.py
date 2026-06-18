from typing import Union
class SumCalculator:
    def calculate_sum(self, a: int | float, b: int | float, c: int | float) -> Union[int, float]:
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(10, 20.5, 30)
    print(result)