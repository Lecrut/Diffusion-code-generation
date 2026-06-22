def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    try:
        sample_base = 14
        sample_height = 7
        triangle_area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle is: {triangle_area}")
    except ValueError as e:
        print(e)