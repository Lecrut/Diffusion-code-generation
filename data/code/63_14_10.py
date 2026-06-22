def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_digits = int(''.join(reversed(str(abs(n)))))
    return sign * reversed_digits

if __name__ == '__main__':
    test_values = [123, -456, 0, 1200]
    for val in test_values:
        print(reverse_integer(val))