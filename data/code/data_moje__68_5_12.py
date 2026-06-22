def dollars_to_cents(dollar_amount):
    dollar_str = str(dollar_amount)
    if '.' in dollar_str:
        dollar_str = dollar_str.replace('.', '')
    else:
        dollar_str += '00'
    cents = int(dollar_str)
    decimal_places = len(dollar_str.split('.')[1]) if '.' in str(dollar_amount) else 0
    if decimal_places == 0:
        cents *= 100
    elif decimal_places == 1:
        cents *= 10
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(1))
    print(dollars_to_cents(1.5))
    print(dollars_to_cents(123.45))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100.00))