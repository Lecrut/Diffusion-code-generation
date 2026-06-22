import math

def compute_cone_volume(radius: float, height: float) -> float:
    return (math.pi * radius * radius * height) / 3.0

if __name__ == '__main__':
    radius_value: float = 2.5
    height_value: float = 4.0
    result: float = compute_cone_volume(radius_value, height_value)
    print(result)