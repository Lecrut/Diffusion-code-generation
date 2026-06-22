def calculate_area(rectangle_width, rectangle_height, triangle_base, triangle_height):
    if not (isinstance(rectangle_width, (int, float)) and isinstance(rectangle_height, (int, float))):
        raise ValueError("Rectangle width and height must be numbers")
    if not (isinstance(triangle_base, (int, float)) and isinstance(triangle_height, (int, float))):
        raise ValueError("Triangle base and height must be numbers")
    
    rectangle_area = rectangle_width * rectangle_height
    triangle_area = 0.5 * triangle_base * triangle_height
    total_area = rectangle_area + triangle_area
    
    return total_area

if __name__ == '__main__':
    result = calculate_area(10, 6, 8, 5)
    print(result)