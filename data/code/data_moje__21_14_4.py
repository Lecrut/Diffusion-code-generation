def get_largest_float(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    val1 = 3.5
    val2 = 12.8
    val3 = 7.2
    result = get_largest_float(val1, val2, val3)
    print(result)