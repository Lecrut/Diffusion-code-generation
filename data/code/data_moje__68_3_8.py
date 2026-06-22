from typing import Union

def dollars_to_cents(amount: Union[int, float]) -> int:
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(amount).__name__}")
    if isinstance(amount, bool):
        raise TypeError("Boolean type is not allowed for numeric amount")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    return int(round(amount * 100))

if __name__ == '__main__':
    result = dollars_to_cents(10.5)
    print(result)