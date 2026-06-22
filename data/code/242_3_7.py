import math

def calculate_hexagon_area(side_length):
    return (3 * math.sqrt(3) / 2) * side_length ** 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    hexagon_side_length = 4
    circle_radius = 3
    
    hexagon_area = calculate_hexagon_area(hexagon_side_length)
    circle_area = calculate_circle_area(circle_radius)
    
    print("--- Shape Area Comparison ---")
    print(f"Hexagon Side Length: {hexagon_side_length}")
    print(f"Calculated Hexagon Area: {hexagon_area:.6f}")
    print("-" * 30)
    print(f"Circle Radius: {circle_radius}")
    print(f"Calculated Circle Area: {circle_area:.6f}")