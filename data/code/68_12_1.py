def dollars_to_cents(dollars: float) -> int:
    return round(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100.01))
    print(dollars_to_cents(-5.25))