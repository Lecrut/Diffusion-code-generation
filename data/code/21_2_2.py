def find_largest(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    val1 = 10
    val2 = 45
    val3 = 30
    result = find_largest(val1, val2, val3)
    print(result)