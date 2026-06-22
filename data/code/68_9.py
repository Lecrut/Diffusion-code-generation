import decimal

def convert_dollars_to_cents(values):
    results = []
    d_100 = decimal.Decimal(100)
    for value in values:
        d_val = decimal.Decimal(str(value))
        c_val = int((d_val * d_100).to_integral_value())
        results.append(c_val)
    return results

if __name__ == '__main__':
    sample_values = [1.0, 1.5, 0.99, 10.255, 0.01]
    output = convert_dollars_to_cents(sample_values)
    for val in output:
        print(val)