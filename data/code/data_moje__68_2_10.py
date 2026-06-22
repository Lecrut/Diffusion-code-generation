def dollars_to_cents(dollars: float) -> int:
    if dollars >= 0:
        return int(round(dollars * 100))
    else:
        return -int(round(abs(dollars) * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(-10.50))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(0.005))