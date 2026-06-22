from typing import Union

def dollars_to_cents(dollars: Union[int, float]) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a numeric type (int or float)")
    if not (dollars == dollars):
        raise ValueError("Input must be a finite number")
    cents = int(round(dollars * 100))
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0))
    print(dollars_to_cents(-5.25))
    print(dollars_to_cents(3))
    try:
        dollars_to_cents("10")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    try:
        dollars_to_cents(float('nan'))
    except ValueError as e:
        print(f"Caught ValueError: {e}")