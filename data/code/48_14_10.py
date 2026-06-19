import math

def calculate_hypotenuse(base, height):
    return math.sqrt(base**2 + height**2)

def calculate_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base_length = 6.0
    height_length = 8.0
    
    hypotenuse_length = calculate_hypotenuse(base_length, height_length)
    triangle_area = calculate_area(base_length, height_length)
    
    print(f"Hypotenuse: {hypotenuse_length}")
    print(f"Area: {triangle_area}")