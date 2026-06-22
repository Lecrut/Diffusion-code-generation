import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def cone_volume(radius: float, height: float) -> float:
    r = Decimal(str(radius))
    h = Decimal(str(height))
    pi = Decimal(math.pi)
    volume = (Decimal('1') / Decimal('3')) * pi * (r ** 2) * h
    return float(volume)

if __name__ == '__main__':
    result = cone_volume(2.5, 4.0)
    print(result)