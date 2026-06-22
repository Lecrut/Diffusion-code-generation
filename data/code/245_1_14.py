import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    return side_length * side_length

def check_areas_equal(circle_radius, square_side_length):
    circle_area = calculate_circle_area(circle_radius)
    square_area = calculate_square_area(square_side_length)
    return circle_area == square_area

if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.0
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {check_areas_equal(r1, l1)}")
    
    r2 = 3.0
    l2 = math.pi * 3.0
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {check_areas_equal(r2, l2)}")
    
    r3 = 1.0
    l3 = math.pi
    print(f"Radius: {r3}, Length: {l3}, Areas Equal: {check_areas_equal(r3, l3)}")