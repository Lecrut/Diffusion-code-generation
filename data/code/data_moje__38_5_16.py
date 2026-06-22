import math

def cone_volume(radius: float, height: float) -> float:
    return math.pi * (radius ** 2) * height / 3.0

if __name__ == '__main__':
    result = cone_volume(2.5, 4.0)
    print(result)