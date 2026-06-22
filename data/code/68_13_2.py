def dollars_to_cents(dollar_amount):
    return int(dollar_amount * 100)

if __name__ == '__main__':
    sample_values = [10.50, -2.75, 0, 999.99]
    for val in sample_values:
        print(dollars_to_cents(val))