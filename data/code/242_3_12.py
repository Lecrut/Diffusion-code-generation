import math

def calculate_hexagon_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def calculate_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2

if __name__ == '__main__':
    hexagon_side_length = 4
    circle_radius = 3
    
    hexagon_area = calculate_hexagon_area(hexagon_side_length)
    circle_area = calculate_circle_area(circle_radius)
    
    print(f"Hexagon Area: {hexagon_area}")
    print(f"Circle Area: {circle_area}")