def herons_formula(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    s = (a + b + c) / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area
if __name__ == '__main__':
    try:
        result1 = herons_formula(3, 4, 5)
        print(f"Area for sides 3, 4, 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = herons_formula(1, 2, 10)
        print(f"Area for sides 1, 2, 10: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = herons_formula(5, 5, 1)
        print(f"Area for sides 5, 5, 1: {result3}")
    except ValueError as e:
        print(f"Error: {e}")