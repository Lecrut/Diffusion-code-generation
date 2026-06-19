def calculate_triangle_perimeter(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    try:
        a = 6
        b = 8
        c = 10
        perimeter = calculate_triangle_perimeter(a, b, c)
        print(perimeter)
    except ValueError as e:
        print(e)