def convert_dollars_to_cents(amount):
    str_amount = str(amount)
    if '.' in str_amount:
        integer_part, decimal_part = str_amount.split('.')
        if len(decimal_part) == 1:
            decimal_part += '0'
        result = int(integer_part + decimal_part)
        if amount < 0:
            result = -result
        return result
    return int(str_amount) * 100

if __name__ == '__main__':
    sample_values = [10.5, 10.05, 10, -15.75, 0.99]
    for val in sample_values:
        print(convert_dollars_to_cents(val))