import math

def calculate_hypotenuse(base, height):
    return math.sqrt(base**2 + height**2)

def calculate_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 9.0
    sample_height = 12.0
    hypotenuse_length = calculate_hypotenuse(sample_base, sample_height)
    triangle_area = calculate_area(sample_base, sample_height)
    print(f"Hypotenuse: {hypotenuse_length}")
    print(f"Area: {triangle_area}")