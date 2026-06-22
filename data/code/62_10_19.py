import math
from typing import List

def get_sorted_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = set()
    limit = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

if __name__ == '__main__':
    sample_number = 28
    result = get_sorted_divisors(sample_number)
    print(result)