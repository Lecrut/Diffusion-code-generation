import math

def calculate_hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def compare_areas(hex_side, circle_radius):
    hex_area = calculate_hexagon_area(hex_side)
    circle_area = calculate_circle_area(circle_radius)
    return hex_area, circle_area

if __name__ == '__main__':
    hex_side_length = 4.0
    circle_radius = 3.0
    hex_area, circle_area = compare_areas(hex_side_length, circle_radius)
    print("--- Shape Area Comparison ---")
    print(f"Hexagon Side Length: {hex_side_length}")
    print(f"Calculated Hexagon Area: {hex_area:.6f}")
    print("-" * 30)
    print(f"Circle Radius: {circle_radius}")
    print(f"Calculated Circle Area: {circle_area:.6f}")