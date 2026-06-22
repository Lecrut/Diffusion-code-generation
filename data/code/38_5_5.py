from decimal import Decimal, getcontext
from typing import Union

getcontext().prec = 50

def compute_cone_volume(radius: Union[float, int, Decimal], height: Union[float, int, Decimal]) -> float:
    r_decimal = Decimal(str(radius))
    h_decimal = Decimal(str(height))
    pi_decimal = Decimal("3.1415926535897932384626433832795028841971693993751")
    volume_decimal = (pi_decimal * (r_decimal ** 2) * h_decimal) / Decimal(3)
    return float(volume_decimal)

if __name__ == '__main__':
    radius_val = 2.5
    height_val = 4.0
    result = compute_cone_volume(radius_val, height_val)
    print(result)