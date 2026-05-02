def triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c
if __name__ == '__main__':
    try:
        print(triangle_perimeter(3, 4, 5))
        print(triangle_perimeter(5, 12, 13))
        print(triangle_perimeter(1, 1, 1))
        print(triangle_perimeter(1, 2, 4))
    except ValueError as e:
        print(f"Error: {e}")