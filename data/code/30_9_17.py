import math

def area_of_circle(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r

if __name__ == '__main__':
    sample_radius = 3.5
    result = area_of_circle(sample_radius)
    print(result)