from typing import Final
from decimal import Decimal

def compute_cone_volume(radius: float, height: float) -> float:
    pi: Final[float] = 3.141592653589793
    return (Decimal(pi) * Decimal(radius) * Decimal(radius) * Decimal(height) / Decimal(3)).quantize(Decimal('1.0000000000000000000000000000')).normalize()

if __name__ == '__main__':
    sample_radius: float = 2.5
    sample_height: float = 4.0
    result: float = float(compute_cone_volume(sample_radius, sample_height))
    print(result)