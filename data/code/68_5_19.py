def dollars_to_cents(amount):
    s = str(amount)
    if '.' in s:
        integer_part, decimal_part = s.split('.')
        decimal_part = decimal_part.ljust(2, '0')[:2]
        result_str = integer_part + decimal_part
    else:
        result_str = s + '00'
    if result_str.startswith('-'):
        return -int(result_str[1:])
    return int(result_str)

if __name__ == '__main__':
    samples = [10.05, 0.99, 100, -5.50, 0.0]
    for val in samples:
        print(dollars_to_cents(val))