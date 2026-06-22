import math

def get_sorted_divisors(n: int) -> list[int]:
    if n < 1:
        return []
    divisors: list[int] = []
    limit: int = int(math.isqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            divisors.append(i)
            other = n // i
            if other != i:
                divisors.append(other)
    return sorted(divisors)

if __name__ == '__main__':
    num: int = 28
    result: list[int] = get_sorted_divisors(num)
    print(result)
    num2: int = 100
    result2: list[int] = get_sorted_divisors(num2)
    print(result2)