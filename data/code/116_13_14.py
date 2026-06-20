from typing import Tuple

class SumCalculator:
    @staticmethod
    def sum_three_ints(numbers: Tuple[int, int, int]) -> int:
        return numbers[0] + numbers[1] + numbers[2]

if __name__ == '__main__':
    sample_values = (7, 8, 9)
    result = SumCalculator.sum_three_ints(sample_values)
    print(result)