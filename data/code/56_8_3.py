import math

def calculate_circumference_and_perimeter(radius, side_length):
    circle_circumference = 2 * math.pi * radius
    square_perimeter = 4 * side_length
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    radius = 5
    side_length = 10
    result = calculate_circumference_and_perimeter(radius, side_length)
    print(result)