def find_largest(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    result = find_largest(3.14, 2.71, 1.62)
    print(result)
    result2 = find_largest(-5.0, -1.0, -3.0)
    print(result2)
    result3 = find_largest(0.0, 0.0, 0.0)
    print(result3)
    result4 = find_largest(100.5, 200.7, 50.3)
    print(result4)