def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.99))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.0))
    print(dollars_to_cents(0.1 + 0.2))