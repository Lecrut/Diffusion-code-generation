from typing import Union

def dollars_to_cents(amount: Union[int, float]) -> int:
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Expected int or float, got {type(amount).__name__}")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(round(amount * 100))

if __name__ == '__main__':
    result = dollars_to_cents(12.345)
    print(result)