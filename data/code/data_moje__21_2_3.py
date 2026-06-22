def get_largest(a: float, b: float, c: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("All arguments must be numeric")
    return a if a >= b and a >= c else b if b >= c else c

if __name__ == '__main__':
    result = get_largest(10, 20, 15)
    print(result)