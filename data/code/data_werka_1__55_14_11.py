def calculate_triangle_perimeter(a, b, c):
    if all(isinstance(side, (int, float)) for side in [a, b, c]):
        return a + b + c
    else:
        raise ValueError("All sides must be numeric")

if __name__ == '__main__':
    try:
        print(calculate_triangle_perimeter(3, 4, 5))
    except ValueError as e:
        print(e)