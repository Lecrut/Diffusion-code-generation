import math

def cone_volume():
    radius = 5
    height = 10
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    result = cone_volume()
    print(result)