from typing import Union
class SumCalculator:
    @staticmethod
    def calculate_sum(a: int | float, b: int | float, c: int | float) -> Union[int, float]:
        return a + b + c
if __name__ == '__main__':
    result = SumCalculator.calculate_sum(10.5, 20, -3.7)
    print(f"Sum of {10.5}, {20} and {-3.7}: {result}")