def heron_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area
if __name__ == '__main__':
    try:
        result1 = heron_formula(3, 4, 5)
        print(f"Area of triangle (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = heron_formula(1, 2, 10)
        print(f"Area of triangle (1, 2, 10): {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = heron_formula(5, 5, 1)
        print(f"Area of triangle (5, 5, 1): {result3}")
    except ValueError as e:
        print(f"Error: {e}")