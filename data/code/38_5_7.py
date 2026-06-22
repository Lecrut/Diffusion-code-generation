from typing import Final

def compute_cone_volume(radius: float, height: float) -> float:
    return (1.0 / 3.0) * 3.141592653589793 * (radius ** 2) * height

if __name__ == '__main__':
    sample_radius: Final[float] = 2.5
    sample_height: Final[float] = 4.0
    print(compute_cone_volume(sample_radius, sample_height))