def dollars_to_cents(amount: float) -> int:
    if amount >= 0:
        return int(round(amount * 100))
    else:
        return -int(round(abs(amount) * 100))

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(-12.34))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(-0.005))