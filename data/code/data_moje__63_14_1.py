def reverse_integer(n):
    sign = 1 if n >= 0 else -1
    reversed_digits = int(''.join(reversed(str(abs(n)))))
    return sign * reversed_digits

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(100))