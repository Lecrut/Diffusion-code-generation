import math

def volume_of_cone(radius: float, height: float) -> float:
    return (1 / 3) * math.pi * radius**2 * height

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    print(volume_of_cone(radius, height))