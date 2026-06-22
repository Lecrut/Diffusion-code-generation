import math

def circle_area(radius):
    if radius < 0:
        return None
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7.5
    area = circle_area(sample_radius)
    if area is not None:
        print(f"Area of circle with radius {sample_radius}: {area}")
    else:
        print("Invalid radius")