import math
from dataclasses import dataclass
from typing import Tuple

@dataclass
class ConeDimensions:
    radius: float
    height: float

def calculate_cone_volume(dims: ConeDimensions) -> float:
    if dims.radius < 0 or dims.height < 0:
        return 0.0
    return (math.pi * dims.radius ** 2 * dims.height) / 3

if __name__ == '__main__':
    cone_dims = ConeDimensions(radius=5.0, height=10.0)
    vol = calculate_cone_volume(cone_dims)
    print(vol)