def dollars_to_cents(dollar_amount):
    return round(dollar_amount * 100)

if __name__ == '__main__':
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(10.00))
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.29))
    print(dollars_to_cents(0.10))