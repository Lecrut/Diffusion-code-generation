def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be positive")
    return side ** 2

def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height

def compare_areas():
    side_length_square = 5
    base_triangle = 4
    height_triangle = 6
    
    area_square = calculate_square_area(side_length_square)
    area_triangle = calculate_triangle_area(base_triangle, height_triangle)
    
    return area_square > area_triangle

if __name__ == '__main__':
    result = compare_areas()
    print(result)