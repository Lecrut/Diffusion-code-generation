def calculate_triangle_perimeter(a, b, c):
    NUMERIC_TYPES = (int, float)
    
    if not all(isinstance(x, NUMERIC_TYPES) for x in [a, b, c]):
        raise ValueError("All sides must be numeric types.")
    if any(x <= 0 for x in [a, b, c]):
        raise ValueError("Side lengths must be positive numbers.")
    
    return a + b + c

if __name__ == '__main__':
    try:
        sample_sides = [(3, 4, 5), (7.5, 9.2, 4.8), (-3, 4, 5)]
        for sides in sample_sides:
            perimeter = calculate_triangle_perimeter(*sides)
            print(f"Perimeter of triangle with sides {sides}: {perimeter}")
    except ValueError as e:
        print(e)