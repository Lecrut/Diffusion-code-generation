def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    print(find_largest(5, 10, 3))
    print(find_largest(-1, -2, -3))
    print(find_largest(100, 100, 50))