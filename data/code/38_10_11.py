import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (math.pi * radius ** 2 * height) / 3

if __name__ == '__main__':
    r = 5
    h = 10
    result = compute_cone_volume(r, h)
    print(result)