def reverse_digits(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_str = ''.join([c for c in str(abs(n))][::-1])
    return sign * int(reversed_str)

if __name__ == '__main__':
    values = [123, -456, 0, 1000, -789]
    results = [reverse_digits(val) for val in values]
    print(results)