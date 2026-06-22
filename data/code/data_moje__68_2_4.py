def dollars_to_cents(dollars: float) -> int:
    sign = -1 if dollars < 0 else 1
    cents = int(abs(dollars) * 100 + 0.5)
    return sign * cents

if __name__ == '__main__':
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(-4.56))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(-0.01))
    print(dollars_to_cents(1.999))
    print(dollars_to_cents(-1.999))