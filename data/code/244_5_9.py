import math

def calculate_area():
    semicircle_radius = 4
    rectangle_length = 5
    rectangle_width = 8
    
    if not (isinstance(semicircle_radius, (int, float)) and isinstance(rectangle_length, (int, float)) and isinstance(rectangle_width, (int, float))):
        raise ValueError("All dimensions must be numbers")
    
    semicircle_area = 0.5 * math.pi * (semicircle_radius ** 2)
    rectangle_area = rectangle_length * rectangle_width
    
    return semicircle_area + rectangle_area

if __name__ == '__main__':
    result = calculate_area()
    print(result)