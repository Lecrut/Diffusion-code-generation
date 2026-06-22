def dollars_to_cents(dollars: float) -> int:
    return round(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(10.99))
    print(dollars_to_cents(0.29))