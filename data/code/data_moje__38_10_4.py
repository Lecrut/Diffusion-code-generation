import math

def compute_cone_volume(radius: float, height: float) -> float:
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive.")
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    fixed_radius: float = 5.0
    fixed_height: float = 10.0
    volume: float = compute_cone_volume(fixed_radius, fixed_height)
    print(volume)