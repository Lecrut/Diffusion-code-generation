import math

def calculate_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    fixed_radius = 5
    fixed_height = 10
    volume = calculate_cone_volume(fixed_radius, fixed_height)
    print(volume)