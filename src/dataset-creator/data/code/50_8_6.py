from typing import Union
class SumCalculator:
    def calculate_sum(self, a: int | float, b: int | float, c: int | float) -> Union[int, float]:
        return a + b + c
if __name__ == '__main__':
    calc = SumCalculator()
    result = calc.calculate_sum(10, 20.5, -3)
    print(result)