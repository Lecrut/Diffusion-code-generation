def dollars_to_cents(amount: float) -> int:
    return int(round(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.999))
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(-5.5))
    print(dollars_to_cents(0.0))