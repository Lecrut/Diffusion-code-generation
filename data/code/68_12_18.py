def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(1.99))
    print(dollars_to_cents(0.00))
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))
    print(dollars_to_cents(0.10))
    print(dollars_to_cents(1.234))
    print(dollars_to_cents(1.235))
    print(dollars_to_cents(99.99))