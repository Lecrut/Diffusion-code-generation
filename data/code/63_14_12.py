def reverse_integer(n):
    if n < 0:
        return -int(''.join(list(reversed(str(-n)))))
    return int(''.join(list(reversed(str(n)))))

if __name__ == '__main__':
    test_values = [123, -456, 0, 987654321]
    for value in test_values:
        print(reverse_integer(value))