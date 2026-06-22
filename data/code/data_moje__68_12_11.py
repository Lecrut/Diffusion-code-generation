import decimal
from decimal import Decimal
from typing import Union

def dollars_to_cents(amount_dollars: Union[float, int, Decimal, str]) -> int:
    if isinstance(amount_dollars, float):
        d = Decimal(str(amount_dollars))
    else:
        d = Decimal(amount_dollars)
    scaled = d * 100
    return int(scaled.to_integral_value(rounding=decimal.ROUND_HALF_EVEN))

if __name__ == '__main__':
    test_values = [1.25, 10.0, 0.01, 99.99, 100.00, 0.1, 1.005]
    for value in test_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")