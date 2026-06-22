def find_largest(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    print(find_largest(3.5, 7.2, 1.8))
    print(find_largest(10.1, 10.1, 10.1))
    print(find_largest(-5.3, -1.2, -9.8))
    print(find_largest(0.0, -0.0, 1.0))