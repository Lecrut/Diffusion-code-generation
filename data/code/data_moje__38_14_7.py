import math

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    volume = calculate_cone_volume(r, h)
    print(volume)