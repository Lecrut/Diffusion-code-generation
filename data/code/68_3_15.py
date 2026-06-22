def dollars_to_cents(dollars: float | int) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError(f"Expected int or float, got {type(dollars).__name__}")
    if isinstance(dollars, bool):
        raise TypeError("Boolean is not a valid numeric type for this conversion")
    if dollars < 0:
        raise ValueError("Dollars cannot be negative")
    cents = round(dollars * 100)
    if cents < 0:
        raise ValueError("Cents cannot be negative")
    return cents

if __name__ == '__main__':
    sample_dollars = 42.5
    result = dollars_to_cents(sample_dollars)
    print(result)