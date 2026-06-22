import math

def calculate_cone_volume(radius, height):
    volume = 1.0 / 3.0 * math.pi * radius ** 2 * height
    return volume
if __name__ == '__main__':
    radius = 5
    height = 10
    volume = calculate_cone_volume(radius, height)
    print(volume)