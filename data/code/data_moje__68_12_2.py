def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(0.10))
    print(dollars_to_cents(0.01))