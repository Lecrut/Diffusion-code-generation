import math

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 7
    height = 5
    volume = calculate_cone_volume(radius, height)
    print(volume)