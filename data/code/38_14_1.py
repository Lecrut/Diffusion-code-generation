import math

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    volume = calculate_cone_volume(sample_radius, sample_height)
    print(volume)