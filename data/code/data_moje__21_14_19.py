def find_largest(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c

if __name__ == '__main__':
    result = find_largest(1.5, 3.2, 2.7)
    print(result)