def dollars_to_cents(dollars):
    cents = int(dollars * 100)
    return cents

if __name__ == '__main__':
    amount = 12.34
    result = dollars_to_cents(amount)
    print(result)