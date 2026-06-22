def convert_dollar_to_cents(dollar_amount):
    dollars_str = str(dollar_amount)
    cents_str = dollars_str.replace('.', '')
    return int(cents_str)

if __name__ == '__main__':
    result = convert_dollar_to_cents(10.50)
    print(result)