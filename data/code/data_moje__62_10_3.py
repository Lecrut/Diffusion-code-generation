from typing import List
import math

def get_divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    divisors = []
    square_root = int(math.isqrt(n))
    for i in range(1, square_root + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    sample_number = 36
    result = get_divisors(sample_number)
    print(result)