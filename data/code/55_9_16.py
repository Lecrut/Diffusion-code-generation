def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.5, 4.2, 5.1)
        print(perimeter)
    except ValueError as e:
        print(e)