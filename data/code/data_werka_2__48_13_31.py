import math

def calculate_hypotenuse_and_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    
    hypotenuse = math.sqrt(base**2 + height**2)
    area = 0.5 * base * height
    return hypotenuse, area

if __name__ == '__main__':
    base_length = 6.0
    height_length = 8.0
    hypotenuse, area = calculate_hypotenuse_and_area(base_length, height_length)
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")