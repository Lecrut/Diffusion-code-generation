from typing import Union

def convert_dollars_to_cents(value: Union[int, float]) -> int:
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric type (int or float).")
    if isinstance(value, float) and (value != value or value == float('inf') or value == float('-inf')):
        raise ValueError("Input cannot be NaN or infinity.")
    if value < 0:
        raise ValueError("Input cannot be negative.")
    total_cents = int(round(value * 100))
    if total_cents != value * 100:
        raise ValueError("Input results in a fractional cent which cannot be represented as an integer.")
    return total_cents

if __name__ == '__main__':
    print(convert_dollars_to_cents(10))
    print(convert_dollars_to_cents(1.50))
    print(convert_dollars_to_cents(0.25))
    print(convert_dollars_to_cents(100.99))