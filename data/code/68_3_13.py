def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric value")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a numeric value, not a boolean")
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100))
    try:
        dollars_to_cents("invalid")
    except TypeError as e:
        print(e)