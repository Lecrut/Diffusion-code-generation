import math

def get_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius1 = 5.0
    sample_radius2 = 7.5
    print(get_area(sample_radius1))
    print(get_area(sample_radius2))