import math

def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    volume = calculate_cone_volume(7, 5)
    print(volume)