import math

def _compute_cone_volume(radius: float, height: float) -> float:
    ONE_THIRD = 1 / 3
    return ONE_THIRD * math.pi * radius ** 2 * height

def calculate_cone_volume(radius: float, height: float) -> float:
    return _compute_cone_volume(radius, height)
if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    result = calculate_cone_volume(sample_radius, sample_height)
    print(result)