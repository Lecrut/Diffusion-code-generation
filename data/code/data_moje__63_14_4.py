def reverse_integer(n):
    sign = -1 if n < 0 else 1
    digits = [d for d in str(abs(n))]
    reversed_digits = digits[::-1]
    reversed_number = int("".join(reversed_digits))
    return sign * reversed_number

if __name__ == '__main__':
    test_values = [123, -456, 0, 9870, -100]
    for value in test_values:
        print(reverse_integer(value))