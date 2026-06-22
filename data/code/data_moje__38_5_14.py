from typing import Final
from decimal import Decimal, ROUND_HALF_EVEN

def compute_cone_volume(radius: float, height: float) -> float:
    precision_radius: Final[Decimal] = Decimal(str(radius))
    precision_height: Final[Decimal] = Decimal(str(height))
    pi_val: Final[Decimal] = Decimal("3.14159265358979323846264338327950288419716939937510")
    radius_squared: Decimal = precision_radius * precision_radius
    volume_decimal: Decimal = (pi_val * radius_squared * precision_height) / Decimal(3)
    return float(volume_decimal.quantize(Decimal("0.0000000000000000001"), rounding=ROUND_HALF_EVEN))

if __name__ == "__main__":
    sample_radius: float = 2.5
    sample_height: float = 4.0
    result: float = compute_cone_volume(sample_radius, sample_height)
    print(result)