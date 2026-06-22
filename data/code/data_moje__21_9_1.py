def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    print(find_largest(3, 7, 2))
    print(find_largest(10, 5, 10))
    print(find_largest(-1, -5, -3))