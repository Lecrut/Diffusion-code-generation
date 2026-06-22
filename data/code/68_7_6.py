def dollars_to_cents(dollars):
    cents = int(round(dollars * 100))
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(12.345))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))