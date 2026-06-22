def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric type")
    if isinstance(dollars, bool):
        raise TypeError("Input must not be a boolean")
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100))
    try:
        dollars_to_cents("10")
    except TypeError as e:
        print(e)
    try:
        dollars_to_cents(None)
    except TypeError as e:
        print(e)