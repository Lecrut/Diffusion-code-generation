def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(123.456))
    print(dollars_to_cents(0.999))
    print(dollars_to_cents(0))