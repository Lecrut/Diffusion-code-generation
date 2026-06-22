import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    result = compute_cone_volume(5, 10)
    print(result)