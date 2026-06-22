def dollars_to_cents(dollars):
    cents = int(round(dollars * 100))
    return cents

if __name__ == '__main__':
    result = dollars_to_cents(5.67)
    print(result)
    result = dollars_to_cents(0.1)
    print(result)
    result = dollars_to_cents(10.00)
    print(result)