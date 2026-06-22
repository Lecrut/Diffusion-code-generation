def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric type")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a numeric type")
    if dollars < 0:
        raise ValueError("Dollars cannot be negative")
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0))
    print(dollars_to_cents(3.14))
    try:
        dollars_to_cents("invalid")
    except TypeError as e:
        print(repr(e))
    try:
        dollars_to_cents(-5)
    except ValueError as e:
        print(repr(e))