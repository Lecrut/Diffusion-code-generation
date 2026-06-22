def dollar_to_cents(amount):
    amount_str = str(amount)
    if '.' in amount_str:
        parts = amount_str.split('.')
        integer_part = parts[0]
        decimal_part = parts[1]
        if len(decimal_part) == 1:
            decimal_part += '0'
        elif len(decimal_part) == 0:
            decimal_part = '00'
        elif len(decimal_part) > 2:
            decimal_part = decimal_part[:2]
        else:
            decimal_part = decimal_part
        result_str = integer_part + decimal_part
        if amount < 0:
            result_str = '-' + result_str.lstrip('-')
        return int(result_str)
    else:
        return int(amount) * 100

if __name__ == '__main__':
    test_values = [10.99, 5.5, 100.0, 1.1, -2.5, 0.01, 0.05]
    for val in test_values:
        print(dollar_to_cents(val))