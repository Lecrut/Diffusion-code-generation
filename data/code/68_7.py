def dollars_to_cents(dollars):
    if dollars < 0:
        sign = -1
        amount = -dollars
    else:
        sign = 1
        amount = dollars
    rounded = int(amount * 100 + 0.5)
    return sign * rounded

if __name__ == '__main__':
    samples = [1.0, 0.575, 0.005, 10.015, -2.5, 100.0, 0.0, 99.995]
    for val in samples:
        result = dollars_to_cents(val)
        print(result)