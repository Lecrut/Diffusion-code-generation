def dollars_to_cents(amount):
    cents = int(amount * 100)
    return cents

if __name__ == '__main__':
    sample_dollars = 12.34
    result = dollars_to_cents(sample_dollars)
    print(result)