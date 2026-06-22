from typing import Union

def dollars_to_cents(dollars: Union[int, float]) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError(f"Expected int or float, got {type(dollars).__name__}")
    if not isinstance(dollars, bool):
        raise TypeError("Expected numeric type, got bool")
    if dollars < 0:
        raise ValueError("Dollars cannot be negative")
    return int(round(dollars * 100))

if __name__ == "__main__":
    sample_values = [10, 2.5, 0.99, 100]
    for value in sample_values:
        print(dollars_to_cents(value))