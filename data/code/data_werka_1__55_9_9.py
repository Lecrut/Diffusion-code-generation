def calculate_triangle_perimeter(a, b, c):
    if not all(x > 0 for x in (a, b, c)):
        raise ValueError("All side lengths must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)