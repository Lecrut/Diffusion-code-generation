import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    r = 2.5
    h = 4.0
    volume = compute_cone_volume(r, h)
    print(volume)