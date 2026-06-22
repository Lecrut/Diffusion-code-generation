import math
from dataclasses import dataclass

@dataclass
class ConeDimensions:
    radius: float
    height: float
    volume: float = 0.0

def compute_cone_volume(dimensions: ConeDimensions) -> ConeDimensions:
    factor = 1 / 3
    dimensions.volume = factor * math.pi * (dimensions.radius ** 2) * dimensions.height
    return dimensions

if __name__ == '__main__':
    cone = ConeDimensions(radius=10, height=20)
    result = compute_cone_volume(cone)
    print(result.volume)