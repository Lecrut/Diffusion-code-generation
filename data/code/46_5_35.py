def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    
    def validate_sides(x, y, z):
        return x + y > z and x + z > y and y + z > x
    
    if not validate_sides(a, b, c):
        raise ValueError("The given sides do not form a valid triangle.")
    
    return a + b + c

if __name__ == '__main__':
    sample_a = 3.5
    sample_b = 4.2
    sample_c = 5.1
    try:
        perimeter = calculate_triangle_perimeter(sample_a, sample_b, sample_c)
        print(perimeter)
    except ValueError as e:
        print(e)