import math

def calculate_area_circle(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def calculate_area_square(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length * side_length

def check_equal_areas(radius, side_length):
    circle_area = calculate_area_circle(radius)
    square_area = calculate_area_square(side_length)
    return math.isclose(circle_area, square_area)

if __name__ == '__main__':
    r1 = 5.0
    l1 = 7.96
    print(f"Radius: {r1}, Side Length: {l1}, Areas Equal: {check_equal_areas(r1, l1)}")
    
    r2 = 3.0
    l2 = math.pi * 3.0
    print(f"Radius: {r2}, Side Length: {l2}, Areas Equal: {check_equal_areas(r2, l2)}")
    
    try:
        r3 = -1.0
        l3 = math.pi
        print(f"Radius: {r3}, Side Length: {l3}, Areas Equal: {check_equal_areas(r3, l3)}")
    except ValueError as e:
        print(e)