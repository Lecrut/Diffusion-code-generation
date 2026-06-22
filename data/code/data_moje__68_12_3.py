def dollars_to_cents(dollars: float) -> int:
    return round(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(1.0))
    print(dollars_to_cents(9.99))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(123.456))