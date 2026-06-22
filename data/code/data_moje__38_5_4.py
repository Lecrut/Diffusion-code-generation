import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    result = compute_cone_volume(2.5, 4.0)
    print(result)