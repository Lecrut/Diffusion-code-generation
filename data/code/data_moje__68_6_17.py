def convert_to_cents(dollar_value):
    return int(round(dollar_value * 100))

if __name__ == '__main__':
    print(convert_to_cents(10.5))
    print(convert_to_cents(10.555))
    print(convert_to_cents(0.005))