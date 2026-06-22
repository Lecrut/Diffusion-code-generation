def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_digits = int("".join(list(reversed(str(abs(n))))))
    return sign * reversed_digits

if __name__ == '__main__':
    test_values = [123, -456, 7890, -2023]
    for value in test_values:
        print(reverse_integer(value))