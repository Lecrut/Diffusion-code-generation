from typing import List
from math import isqrt

def get_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = []
    upper_bound = isqrt(n)
    for i in range(1, upper_bound + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_number = 84
    result = get_divisors(sample_number)
    print(result)