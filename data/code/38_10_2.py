import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    RADIUS = 5
    HEIGHT = 10
    result = compute_cone_volume(RADIUS, HEIGHT)
    print(result)