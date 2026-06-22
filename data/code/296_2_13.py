def are_proportional(a, b, c, d):
    if b == 0 or d == 0:
        raise ValueError("Cannot calculate proportion when any denominator is zero")
    return a * d == b * c

if __name__ == '__main__':
    try:
        result = are_proportional(10, 4, 5, 2)
        print(f"Are the numbers proportional? {result}")
    except ValueError as e:
        print(e)