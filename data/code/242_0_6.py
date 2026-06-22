import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    
    circ_area = calculate_circle_area(circle_radius)
    sq_area = calculate_square_area(square_side_length)
    
    print(f"Circle area: {circ_area}")
    print(f"Square area: {sq_area}")
    
    if circ_area > sq_area:
        print("The circle has a larger area.")