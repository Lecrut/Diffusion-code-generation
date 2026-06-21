import math

def calculate_hypotenuse(base, height):
    return math.sqrt(base**2 + height**2)

def calculate_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base = 6.0
    height = 8.0
    
    hypotenuse = calculate_hypotenuse(base, height)
    area = calculate_area(base, height)
    
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")