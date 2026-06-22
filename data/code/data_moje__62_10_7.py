from typing import List
import math

def get_divisors(number: int) -> List[int]:
    if number == 0:
        return []
    if number < 0:
        number = -number
    divisors = set()
    limit = int(math.isqrt(number))
    for i in range(1, limit + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return sorted(list(divisors))

if __name__ == '__main__':
    test_number = 210
    result = get_divisors(test_number)
    print(result)