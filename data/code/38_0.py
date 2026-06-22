import math

def compute_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = compute_cone_volume(sample_radius, sample_height)
    print(result)