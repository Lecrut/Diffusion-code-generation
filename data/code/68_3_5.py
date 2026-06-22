def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a number")
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if dollars < 0:
        raise ValueError("Dollars cannot be negative")
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0))
    print(dollars_to_cents(1.99))
    print(dollars_to_cents(100))
    try:
        dollars_to_cents("10")
    except TypeError as e:
        print(e)
    try:
        dollars_to_cents(-5)
    except ValueError as e:
        print(e)