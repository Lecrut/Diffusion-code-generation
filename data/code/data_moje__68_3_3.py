def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric value (int or float)")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a numeric value (int or float), not bool")
    if dollars < 0:
        raise ValueError("Dollars cannot be negative")
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1))
    print(dollars_to_cents(2.50))
    print(dollars_to_cents(0))
    print(dollars_to_cents(1.99))
    print(dollars_to_cents(10.0))
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0.99))
    try:
        dollars_to_cents(-1.0)
    except ValueError as e:
        print(e)
    try:
        dollars_to_cents("10")
    except TypeError as e:
        print(e)
    try:
        dollars_to_cents(True)
    except TypeError as e:
        print(e)