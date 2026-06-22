import math
import typing

def get_sorted_divisors(n: int) -> typing.List[int]:
    if n <= 0:
        return []
    
    divisors: typing.List[int] = []
    limit: int = int(math.isqrt(n))
    
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    return divisors

if __name__ == '__main__':
    n = 100
    result = get_sorted_divisors(n)
    print(result)
    
    n = 13
    result = get_sorted_divisors(n)
    print(result)