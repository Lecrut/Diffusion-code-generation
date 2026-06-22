def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    FIRST = 42
    SECOND = 99
    THIRD = 5
    result = find_largest(FIRST, SECOND, THIRD)
    print(result)
    print(find_largest(0, 1, -1))