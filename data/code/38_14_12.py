import math

def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    print(cone_volume(sample_radius, sample_height))