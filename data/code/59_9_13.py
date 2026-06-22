from typing import Union

def sum_digits(number: int) -> int:
    total: int = 0
    n: int = abs(number)
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    large_integer: int = 123456789012345678901234567890
    result: int = sum_digits(large_integer)
    print(result)