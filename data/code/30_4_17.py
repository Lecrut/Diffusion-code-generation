import math

def compute_circle_area(radius):
    if radius < 0:
        return -1.0
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_value = 10
    computed_area = compute_circle_area(radius_value)
    print(computed_area)