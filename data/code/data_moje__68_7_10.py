def dollars_to_cents(dollars):
    sign = 1
    if dollars < 0:
        sign = -1
        dollars = -dollars
    whole = int(dollars)
    frac = dollars - whole
    cents_part = int(frac * 100 + 0.5)
    if cents_part >= 100:
        whole += 1
        cents_part -= 100
    total_cents = sign * (whole * 100 + cents_part)
    return total_cents

if __name__ == '__main__':
    print(dollars_to_cents(10.99))
    print(dollars_to_cents(-5.50))
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(99.995))