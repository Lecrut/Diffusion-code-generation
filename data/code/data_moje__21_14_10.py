def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    val1 = 3.5
    val2 = 7.2
    val3 = 2.8
    result = find_largest(val1, val2, val3)
    print(result)