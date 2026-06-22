import math

def volume_of_cone():
    radius = 3.0
    height = 5.0
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    print(volume_of_cone())