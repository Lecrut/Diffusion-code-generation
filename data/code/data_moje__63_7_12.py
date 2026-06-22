def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_val = 0
    while n > 0:
        reversed_val = reversed_val * 10 + n % 10
        n //= 10
    return sign * reversed_val

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-9870))
    print(reverse_integer(0))