def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    val3 = 5
    result = find_greatest(val1, val2, val3)
    print(result)

    val1 = 3
    val2 = 8
    val3 = 12
    result = find_greatest(val1, val2, val3)
    print(result)

    val1 = 50
    val2 = 50
    val3 = 10
    result = find_greatest(val1, val2, val3)
    print(result)