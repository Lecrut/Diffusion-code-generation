import math

def calculate_cone_volume(radius, height):
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    radius = 7
    height = 5
    volume = calculate_cone_volume(radius, height)
    print(volume)