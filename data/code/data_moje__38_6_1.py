import math

def compute_cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    print(compute_cone_volume(1, 3))