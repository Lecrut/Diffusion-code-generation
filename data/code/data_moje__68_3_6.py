def dollars_to_cents(dollars: float | int) -> int:
    if isinstance(dollars, bool):
        raise TypeError("Input must be a number, not bool")
    if not isinstance(dollars, (int, float)):
        raise TypeError(f"Expected int or float, got {type(dollars).__name__}")
    if not (-1e15 < dollars < 1e15):
        raise ValueError("Input value is out of supported range")
    if dollars != dollars:
        raise ValueError("Input must not be NaN")
    if dollars == float('inf') or dollars == float('-inf'):
        raise ValueError("Input must not be Infinity")
    cents = round(dollars * 100)
    return cents

if __name__ == '__main__':
    result = dollars_to_cents(12.34)
    print(result)
    result2 = dollars_to_cents(0)
    print(result2)
    result3 = dollars_to_cents(-5.50)
    print(result3)