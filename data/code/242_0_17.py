import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 6
    
    try:
        circle_area = calculate_circle_area(circle_radius)
        square_area = calculate_square_area(square_side_length)
        
        print(f"Circle area: {circle_area}")
        print(f"Square area: {square_area}")
        
        if circle_area > square_area:
            print("The circle has a larger area.")
        else:
            print("The square has a larger area or they are equal.")
    
    except ValueError as e:
        print(e)