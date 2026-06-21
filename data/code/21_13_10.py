def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.1
    val3 = 15.9
    result = find_max(val1, val2, val3)
    print(result)