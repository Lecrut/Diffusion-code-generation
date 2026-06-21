def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    result = find_largest(10, 25, 15)
    print(result)
    result2 = find_largest(-5, -1, -10)
    print(result2)
    result3 = find_largest(100, 100, 50)
    print(result3)