def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_digits = int("".join(reversed(str(abs(n)))))
    return sign * reversed_digits

if __name__ == '__main__':
    test_cases = [123, -456, 120, 0, -987654321]
    for value in test_cases:
        print(reverse_integer(value))