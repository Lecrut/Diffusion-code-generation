def calculate_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("Side lengths must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)