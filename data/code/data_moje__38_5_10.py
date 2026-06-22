import math

def compute_cone_volume(radius: float, height: float) -> float:
    return math.pi * radius ** 2 * height / 3.0

if __name__ == '__main__':
    radius = 2.5
    height = 4.0
    volume = compute_cone_volume(radius, height)
    print(volume)