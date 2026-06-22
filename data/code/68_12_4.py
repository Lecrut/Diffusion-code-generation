from typing import Final
import math

CENTS_PER_DOLLAR: Final[int] = 100

def convert_dollars_to_cents(amount: float) -> int:
    scaled_value: float = amount * CENTS_PER_DOLLAR
    return math.floor(scaled_value + 0.5)

if __name__ == '__main__':
    results: list[int] = [
        convert_dollars_to_cents(0.01),
        convert_dollars_to_cents(1.50),
        convert_dollars_to_cents(3.333),
        convert_dollars_to_cents(100.00),
        convert_dollars_to_cents(0.005),
    ]
    for res in results:
        print(res)