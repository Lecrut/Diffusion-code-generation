import math

def calculate_diagonal(length, width):
    return math.sqrt(length ** 2 + width ** 2)

def calculate_radius(circumference):
    return circumference / (2 * math.pi)

if __name__ == '__main__':
    rectangle_length = 3
    rectangle_width = 4
    circle_circumference = 10

    diagonal = calculate_diagonal(rectangle_length, rectangle_width)
    radius = calculate_radius(circle_circumference)

    ratio = diagonal / radius
    print(ratio)