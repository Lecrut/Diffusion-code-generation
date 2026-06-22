from typing import List
import math

def get_sorted_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = []
    sqrt_n = int(math.isqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    number = 100
    result = get_sorted_divisors(number)
    print(result)