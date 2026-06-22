def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.0))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(10.105))