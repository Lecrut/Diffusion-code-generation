def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    for side in sides:
        if not isinstance(side, (int, float)):
            raise TypeError("Side lengths must be numeric.")
        if side <= 0:
            raise ValueError("Side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    result = calculate_triangle_perimeter(3, 4, 5)
    print(result)