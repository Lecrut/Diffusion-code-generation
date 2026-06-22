def dollars_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(1.00))
    print(dollars_to_cents(12.345))
    print(dollars_to_cents(12.3456))
    print(dollars_to_cents(99.99))
    print(dollars_to_cents(0.995))
    print(dollars_to_cents(0.994))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(1.004))
    print(dollars_to_cents(10.00))