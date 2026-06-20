from typing import Tuple

class SumCalculator:
    def sum_three_integers(self, numbers: Tuple[int, int, int]) -> int:
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_three_integers((1, 2, 3))
    print(result)