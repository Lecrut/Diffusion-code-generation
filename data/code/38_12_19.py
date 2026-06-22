import math

def calculate_cone_volume():
    radius = 3
    height = 5
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    result = calculate_cone_volume()
    print(result)