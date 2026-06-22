import math

def volume_of_cone(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    r = 8
    h = 11
    vol = volume_of_cone(r, h)
    print(f"{vol:.2f}")