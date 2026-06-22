def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    val3 = 15
    print(find_greatest(val1, val2, val3))
    print(find_greatest(5, 3, 8))
    print(find_greatest(7, 7, 7))