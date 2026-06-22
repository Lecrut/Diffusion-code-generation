def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)

if __name__ == '__main__':
    test_values = [123, -456, 1200, 0]
    results = [reverse_integer(val) for val in test_values]
    print(results)