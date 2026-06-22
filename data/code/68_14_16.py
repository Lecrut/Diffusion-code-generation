def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be an integer or float")
    if dollars < 0:
        raise ValueError("Input must be non-negative")
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(0))
    print(dollars_to_cents(1))
    print(dollars_to_cents(1.5))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100))
    print(dollars_to_cents(3.14159))