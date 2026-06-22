def dollar_to_cents(dollar_amount):
    return round(dollar_amount * 100)

if __name__ == '__main__':
    print(dollar_to_cents(0.1 + 0.2))
    print(dollar_to_cents(10.0))
    print(dollar_to_cents(99.995))