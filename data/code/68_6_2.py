def dollars_to_cents(dollars):
    return round(dollars * 100)

if __name__ == '__main__':
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(1.004))
    print(dollars_to_cents(0.5))
    print(dollars_to_cents(10.125))
    print(dollars_to_cents(10.135))
    print(dollars_to_cents(-1.005))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(99.999))
    print(dollars_to_cents(123.456))