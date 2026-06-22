import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def compute_cone_volume(radius: float, height: float) -> float:
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = _precise_pi(50)
    volume = (Decimal('1') / Decimal('3')) * pi * (r ** 2) * h
    return float(volume)

def _precise_pi(precision: int) -> Decimal:
    getcontext().prec = precision + 10
    one = Decimal(1)
    pi = Decimal(0)
    k = 0
    while True:
        term = one / (Decimal(16) ** k) * (
            Decimal(4) / (8 * k + 1) -
            Decimal(2) / (8 * k + 4) -
            Decimal(1) / (8 * k + 5) -
            Decimal(1) / (8 * k + 6)
        )
        new_pi = pi + term
        if new_pi == pi:
            break
        pi = new_pi
        k += 1
    getcontext().prec = precision
    return pi + 0

if __name__ == '__main__':
    result = compute_cone_volume(2.5, 4.0)
    print(result)