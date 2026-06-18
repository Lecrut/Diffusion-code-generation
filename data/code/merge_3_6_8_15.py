from typing import Any
import math

def simple_weight_diff(a: float | int, b: float | int) -> float:
    """Calculate absolute weight difference between two values."""
    return abs(float(a) - float(b))

if __name__ == '__main__':
    val1 = 50.234
    val2 = 98.765 * math.pi
    diff = simple_weight_diff(val1, val2)
    print(f"Weight difference: {diff:.6f}")