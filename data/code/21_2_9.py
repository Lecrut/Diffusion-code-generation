def find_largest(a: float, b: float, c: float) -> float:
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    print(find_largest(3, 7, 2))
    print(find_largest(-1, -5, -3))
    print(find_largest(10, 10, 10))
    print(find_largest(1.5, 2.5, 0.5))