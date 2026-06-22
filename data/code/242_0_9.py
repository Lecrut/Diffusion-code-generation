import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

def compare_areas(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    
    print(f"Circle Radius: {circle_radius}")
    print(f"Square Side Length: {square_side_length}")
    print("-" * 30)
    print(f"Area of Circle: {circle_area:.2f}")
    print(f"Area of Square: {square_area:.2f}")
    
    if circle_area > square_area:
        print("The circle has a larger area.")
    elif circle_area < square_area:
        print("The square has a larger area.")
    else:
        print("Both shapes have the same area.")

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    compare_areas(circle_radius, square_side_length)