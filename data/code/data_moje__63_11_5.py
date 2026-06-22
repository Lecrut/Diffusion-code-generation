def reverse_integer(n):
    s = str(n)
    if s[0] == '-':
        reversed_s = '-' + s[1:][::-1]
    else:
        reversed_s = s[::-1]
    return int(reversed_s)

if __name__ == '__main__':
    test_values = [123, -456, 0, 9800, -1020304]
    for value in test_values:
        result = reverse_integer(value)
        print(result)