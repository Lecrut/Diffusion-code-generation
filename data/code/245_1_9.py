import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive")

def validate_length(length):
    if length <= 0:
        raise ValueError("Length must be positive")

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_square_area(length):
    return length * length

def check_equal_area(radius, length):
    validate_radius(radius)
    validate_length(length)
    
    circle_area = calculate_circle_area(radius)
    square_area = calculate_square_area(length)
    
    return math.isclose(circle_area, square_area)

if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.96
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {check_equal_area(r1, l1)}")
    
    r2 = 3.0
    l2 = math.pi * 3.0
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {check_equal_area(r2, l2)}")
    
    r3 = 1.0
    l3 = math.pi
    print(f"Radius: {r3}, Length: {l3}, Areas Equal: {check_equal_area(r3, l3)}")