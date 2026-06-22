import math
from typing import Union

Number = Union[int, float]

def compute_cone_volume(radius: Number, height: Number) -> float:
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    fixed_radius = 5
    fixed_height = 10
    volume = compute_cone_volume(fixed_radius, fixed_height)
    print(volume)