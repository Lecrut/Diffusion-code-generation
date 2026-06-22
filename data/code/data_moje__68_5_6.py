def dollar_to_cents(amount):
    s = str(amount)
    if '.' in s:
        s = s.replace('.', '')
        parts = s.split('.')
        if len(parts[1]) < 2:
            s += '0' * (2 - len(parts[1]))
    else:
        s += '00'
    return int(s)

if __name__ == '__main__':
    test_values = [1.25, 10.0, 0.99, 5.1, 100.50, 0.5, 1]
    for val in test_values:
        result = dollar_to_cents(val)
        print(f"{val} -> {result}")