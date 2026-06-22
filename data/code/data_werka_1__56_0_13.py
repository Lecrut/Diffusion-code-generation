import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

def square_area(side_length):
    return side_length ** 2

def square_perimeter(side_length):
    return 4 * side_length

if __name__ == '__main__':
    circle_radius = 5
    square_side_length = 10
    
    print("Circle Area:", circle_area(circle_radius))
    print("Circle Perimeter:", circle_perimeter(circle_radius))
    print("Square Area:", square_area(square_side_length))
    print("Square Perimeter:", square_perimeter(square_side_length))