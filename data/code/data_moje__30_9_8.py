import math
def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius
if __name__ == '__main__':
    sample_radius = 12.5
    computed_area = area_of_circle(sample_radius)
    print(computed_area)