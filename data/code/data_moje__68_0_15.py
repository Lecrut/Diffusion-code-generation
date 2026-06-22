def dollars_to_cents(amount):
    return int(round(amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(10.01))
    print(dollars_to_cents(10.99))
    print(dollars_to_cents(0.10))
    print(dollars_to_cents(0.29))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(1.004))
    print(dollars_to_cents(99.999))