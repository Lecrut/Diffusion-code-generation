def dollars_to_cents(dollars: float) -> int:
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.23))
    print(dollars_to_cents(-1.23))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(-0.005))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(1.005))