def find_largest(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All arguments must be numeric")
    return a if a > b and a > c else (b if b > a and b > c else c)

if __name__ == '__main__':
    print(find_largest(10, 25, 15))
    print(find_largest(-5, -1, -10))
    print(find_largest(3.14, 2.71, 1.41))
    print(find_largest(100, 100, 100))