import math

def circle_area(radius: float) -> float:
    squared_radius = radius * radius
    area = math.pi * squared_radius
    return area

if __name__ == '__main__':
    sample_radius = 12.5
    computed_area = circle_area(sample_radius)
    print(computed_area)