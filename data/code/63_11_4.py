def reverse_integer(n):
    s = str(n)
    if s.startswith('-'):
        return -int(s[1:][::-1])
    return int(s[::-1])

if __name__ == '__main__':
    test_values = [123, -456, 7890, 0, -100]
    for val in test_values:
        result = reverse_integer(val)
        print(result)