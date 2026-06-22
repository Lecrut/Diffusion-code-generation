def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(3.99))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(99.99))
    print(dollars_to_cents(1234567.89))
    print(dollars_to_cents(-5.50))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(0.004))