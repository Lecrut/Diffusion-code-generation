def dollars_to_cents(dollars):
    cents = dollars * 100
    return int(abs(cents))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(-5.25))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(99.99))