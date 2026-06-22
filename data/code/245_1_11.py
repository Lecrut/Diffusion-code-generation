import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    return side_length ** 2

def compare_areas(circle_radius, square_side):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side)
    return circle_area == square_area

if __name__ == '__main__':
    r1 = 5.0
    l1 = math.pi * 2.5
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {compare_areas(r1, l1)}")
    
    r2 = 4.0
    l2 = 8.0
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {compare_areas(r2, l2)}")