def find_largest(a: float, b: float, c: float) -> float:
    return a if (a >= b and a >= c) else (b if b >= c else c)

if __name__ == '__main__':
    result = find_largest(10, 20, 15)
    print(result)