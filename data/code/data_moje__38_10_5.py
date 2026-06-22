import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1.0 / 3.0) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    radius = 5
    height = 10
    volume = compute_cone_volume(radius, height)
    print(volume)