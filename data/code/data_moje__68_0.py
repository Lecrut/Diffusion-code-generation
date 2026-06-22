def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0.10))
    print(dollars_to_cents(0.15))
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(1.234))
    print(dollars_to_cents(1.235))
    print(dollars_to_cents(1.245))
    print(dollars_to_cents(10.999))
    print(dollars_to_cents(-1.234))
    print(dollars_to_cents(-1.235))