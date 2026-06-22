def reverse_integer(n: int) -> int:
    if n < 0:
        s = str(n)
        reversed_s = '-' + s[1:][::-1]
        return int(reversed_s)
    reversed_s = str(n)[::-1]
    return int(reversed_s)

if __name__ == '__main__':
    test_values = [123, -456, 0, 700, -3050]
    for value in test_values:
        result = reverse_integer(value)
        print(result)