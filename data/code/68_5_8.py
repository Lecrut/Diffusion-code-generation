def dollars_to_cents(amount):
    s = str(amount)
    if '.' in s:
        parts = s.split('.')
        integer_part = parts[0]
        fractional_part = parts[1]
        if len(fractional_part) == 1:
            fractional_part += '0'
        elif len(fractional_part) > 2:
            fractional_part = fractional_part[:2]
        cents_str = integer_part + fractional_part
    else:
        cents_str = s + '00'
    
    if s.startswith('-'):
        return -int(cents_str)
    return int(cents_str)

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(0.5))
    print(dollars_to_cents(-5.60))
    print(dollars_to_cents(100))