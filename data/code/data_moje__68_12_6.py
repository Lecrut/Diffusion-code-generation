from typing import Union

def dollars_to_cents(amount: float) -> int:
    return int(round(amount * 100))

if __name__ == '__main__':
    test_values = [10.0, 19.99, 0.01, 100.5, 0.001, 1234.567]
    for value in test_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")