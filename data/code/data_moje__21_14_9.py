def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    val1 = 15.5
    val2 = 23.7
    val3 = 9.2
    result = find_largest(val1, val2, val3)
    print(result)