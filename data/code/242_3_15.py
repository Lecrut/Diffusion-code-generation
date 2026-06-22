import math

def calculate_hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def compare_areas(hexagon_side, circle_radius):
    hexagon_area = calculate_hexagon_area(hexagon_side)
    circle_area = calculate_circle_area(circle_radius)
    return hexagon_area, circle_area, hexagon_area > circle_area

if __name__ == '__main__':
    hexagon_side_length = 4.0
    circle_radius = 3.0
    hexagon_area, circle_area, is_hex_larger = compare_areas(hexagon_side_length, circle_radius)
    print("--- Shape Area Comparison ---")
    print(f"Hexagon Side Length: {hexagon_side_length}")
    print(f"Calculated Hexagon Area: {hexagon_area:.4f}")
    print("-" * 30)
    print(f"Circle Radius: {circle_radius}")
    print(f"Calculated Circle Area: {circle_area:.4f}")
    if is_hex_larger:
        print("Hexagon has a larger area.")
    else:
        print("Circle has a larger area or they are equal.")