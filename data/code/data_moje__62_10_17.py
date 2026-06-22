from math import isqrt
from typing import List

def get_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    hard_coded_number = 28
    result = get_divisors(hard_coded_number)
    print(result)