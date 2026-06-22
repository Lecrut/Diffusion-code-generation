def dollars_to_cents(amount):
    return int(round(amount * 100))

if __name__ == '__main__':
    sample_dollars = 123.456
    result_cents = dollars_to_cents(sample_dollars)
    print(result_cents)