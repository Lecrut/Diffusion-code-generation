import math

def calculate_cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 3
    height = 5
    volume = calculate_cone_volume(radius, height)
    print(volume)