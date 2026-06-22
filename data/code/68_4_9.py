def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if dollars < 0:
        raise ValueError("Input must be non-negative")
    return int(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(42.5))
    print(dollars_to_cents(7.01))
    print(dollars_to_cents(0))