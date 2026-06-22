def get_highest_value(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    val3 = 4.5
    result = get_highest_value(val1, val2, val3)
    print(result)