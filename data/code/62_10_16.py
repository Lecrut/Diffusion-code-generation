from typing import List
import math

def get_sorted_divisors(n: int) -> List[int]:
    if n == 0:
        return []
    if n < 0:
        n = -n
    divisors: List[int] = []
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_number = 100
    result = get_sorted_divisors(sample_number)
    print(result)