import math

def calculate_cone_volume(radius: float, height: float) -> float:
    if radius <= 0:
        raise ValueError("Radius must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    base_area = math.pi * radius * radius
    volume = (base_area * height) / 3
    return volume

if __name__ == '__main__':
    r = 3.0
    h = 9.0
    result = calculate_cone_volume(r, h)
    print(result)