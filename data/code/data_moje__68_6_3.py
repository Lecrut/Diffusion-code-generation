def dollars_to_cents(dollars):
    cents = round(dollars * 100)
    return int(cents)

if __name__ == '__main__':
    print(dollars_to_cents(10.995))
    print(dollars_to_cents(0.505))
    print(dollars_to_cents(1.0))
    print(dollars_to_cents(3.335))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(0.015))