import math

def calculate_triangle_properties(base, height):
    hypotenuse = math.sqrt(base**2 + height**2)
    area = 0.5 * base * height
    return hypotenuse, area

if __name__ == '__main__':
    base = 6.0
    height = 8.0
    hypotenuse, area = calculate_triangle_properties(base, height)
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")