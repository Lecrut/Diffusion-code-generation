def convert_to_cents(dollar_amount):
    if dollar_amount < 0:
        return -int(round(-dollar_amount * 100))
    return int(round(dollar_amount * 100))

if __name__ == '__main__':
    sample_amounts = [10.50, 0.01, -5.75, 0, 100.99]
    for amount in sample_amounts:
        cents = convert_to_cents(amount)
        print(cents)