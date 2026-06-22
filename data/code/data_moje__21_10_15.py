def find_largest(a, b, c):
    if not all(isinstance(x, int) for x in (a, b, c)):
        raise TypeError("All arguments must be integers")
    return max(a, b, c)

if __name__ == '__main__':
    VAL_1 = 42
    VAL_2 = 99
    VAL_3 = 17
    result = find_largest(VAL_1, VAL_2, VAL_3)
    print(result)