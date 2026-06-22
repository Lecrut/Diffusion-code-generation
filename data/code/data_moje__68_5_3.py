def dollars_to_cents(dollar_amount):
    s = str(dollar_amount)
    s = s.replace('.', '')
    return int(s)

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(0.99))
    print(dollars_to_cents(100.00))
    print(dollars_to_cents(12.345))