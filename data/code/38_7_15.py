import math

def calculate_cone_volume(radius, height):
    volume = (1.0 / 3.0) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    sample_radius = 7
    sample_height = 5
    result = calculate_cone_volume(sample_radius, sample_height)
    print(result)