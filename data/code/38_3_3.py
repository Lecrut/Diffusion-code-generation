import math

def cone_volume(radius, height):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    if height <= 0:
        raise ValueError("Height must be positive.")
    return (math.pi * radius ** 2 * height) / 3.0

if __name__ == '__main__':
    r = 4
    h = 12
    print(cone_volume(r, h))