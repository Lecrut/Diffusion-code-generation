def find_largest(a, b, c):
    return a if (a >= b and a >= c) else (b if b >= c else c)

if __name__ == '__main__':
    print(find_largest(10, 42, 7))
    print(find_largest(-5, -2, -10))
    print(find_largest(3.5, 3.5, 2.1))