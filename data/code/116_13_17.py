from typing import Tuple

def sum_three_ints(numbers: Tuple[int, int, int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    result = sum_three_ints((10, 20, 30))
    print(result)