def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(99.999))