import math

def compute_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return (1/3) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    volume = compute_cone_volume(r, h)
    print(volume)