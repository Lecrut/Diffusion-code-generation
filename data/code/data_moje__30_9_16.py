import math

def circle_area(radius):
    squared_radius = radius * radius
    computed_area = math.pi * squared_radius
    return computed_area

if __name__ == '__main__':
    test_radius = 3.5
    result = circle_area(test_radius)
    print(result)