from math import pi
from decimal import Decimal, getcontext

def compute_cone_volume(radius: float, height: float) -> Decimal:
    getcontext().prec = 50
    r = Decimal(str(radius))
    h = Decimal(str(height))
    return (Decimal('1') / Decimal('3')) * Decimal(str(pi)) * r ** 2 * h

if __name__ == '__main__':
    result = compute_cone_volume(2.5, 4.0)
    print(result)