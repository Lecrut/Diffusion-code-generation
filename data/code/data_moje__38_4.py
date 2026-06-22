import math

def calculate_cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    r = 6
    h = 9
    volume = calculate_cone_volume(r, h)
    print(volume)