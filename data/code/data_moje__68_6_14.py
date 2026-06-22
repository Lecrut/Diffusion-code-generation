def dollars_to_cents(dollar_value):
    return int(round(dollar_value * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(2.505))
    print(dollars_to_cents(0.125))
    print(dollars_to_cents(10.00))