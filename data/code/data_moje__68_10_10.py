def dollars_to_cents(dollars_str):
    parts = dollars_str.split('.')
    whole_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else ''
    if fractional_part:
        fractional_part = (fractional_part + '00')[:2]
    else:
        fractional_part = '00'
    cents = int(whole_part) * 100 + int(fractional_part)
    return cents

if __name__ == '__main__':
    sample_values = ['0.00', '1.23', '10.50', '100.00', '0.01', '12345.67', '999.99']
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)