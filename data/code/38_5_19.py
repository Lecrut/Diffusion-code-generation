import math
from decimal import Decimal, getcontext

def compute_cone_volume(radius: float, height: float) -> float:
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(math.pi)
    volume = Decimal('1') / Decimal('3') * pi * r ** 2 * h
    return float(volume)

if __name__ == '__main__':
    result = compute_cone_volume(2.5, 4.0)
    print(result)