import math

def compute_cone_volume(radius: float, height: float) -> float:
    base_area = math.pi * (radius ** 2)
    volume = (1 / 3) * base_area * height
    return volume

if __name__ == '__main__':
    r = 2.5
    h = 4.0
    vol = compute_cone_volume(r, h)
    print(vol)