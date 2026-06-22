from typing import List
import math

def get_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = set()
    sqrt_n = int(math.isqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    number = 100
    result = get_divisors(number)
    print(result)