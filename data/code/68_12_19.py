from typing import Union

def dollars_to_cents(amount: float) -> int:
    return int(round(amount * 100))

if __name__ == '__main__':
    samples = [1.00, 0.99, 1.15, 0.10, 123.456]
    for s in samples:
        print(dollars_to_cents(s))