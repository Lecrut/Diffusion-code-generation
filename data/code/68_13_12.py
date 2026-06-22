def dollars_to_cents(dollar_amount):
    return int(dollar_amount * 100)

if __name__ == '__main__':
    sample_amounts = [10.50, -5.25, 0.00, 100.00, -0.01]
    for amount in sample_amounts:
        result = dollars_to_cents(amount)
        print(result)