def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(0.505))
    print(dollars_to_cents(10.0))
    print(dollars_to_cents(0.004))
    print(dollars_to_cents(0.006))
    print(dollars_to_cents(123.456))