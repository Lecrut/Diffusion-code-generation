def convert_dollar_to_cents(dollar_amount_str):
    if '.' in dollar_amount_str:
        integer_part, fractional_part = dollar_amount_str.split('.')
        fractional_part = (fractional_part + '00')[:2].ljust(2, '0')
    else:
        integer_part = dollar_amount_str
        fractional_part = '00'
    
    if not integer_part:
        integer_part = '0'
    
    total_cents = int(integer_part) * 100 + int(fractional_part)
    return total_cents

if __name__ == '__main__':
    samples = ['10.50', '0.99', '100', '0.05']
    for sample in samples:
        result = convert_dollar_to_cents(sample)
        print(result)