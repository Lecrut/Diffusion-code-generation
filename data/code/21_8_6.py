def get_largest(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = get_largest(10, 20, 15)
    print(result)