import math

PI = math.pi

def compute_cone_volume(radius: float, height: float) -> float:
    base_area = PI * radius ** 2
    volume = base_area * height / 3.0
    return volume

if __name__ == '__main__':
    sample_radius = 15
    sample_height = 30
    computed_value = compute_cone_volume(sample_radius, sample_height)
    print(computed_value)