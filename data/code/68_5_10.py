def dollar_to_cents(dollar_amount):
    amount_str = f"{dollar_amount:.2f}"
    cents_str = amount_str.replace('.', '')
    return int(cents_str)

if __name__ == '__main__':
    sample_amounts = [12.34, 0.99, 5.00, 100.10, 0.01]
    for amount in sample_amounts:
        print(dollar_to_cents(amount))