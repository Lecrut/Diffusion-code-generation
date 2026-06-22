def dollars_to_cents(dollars):
    sign = 1 if dollars >= 0 else -1
    abs_dollars = abs(dollars)
    cents = int(abs_dollars * 100 + 0.5) * sign
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(-0.005))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(100.999))