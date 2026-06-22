def dollars_to_cents(dollar_value):
    cents = round(dollar_value * 100)
    return int(cents)

if __name__ == '__main__':
    sample_values = [10.995, 10.994, 10.996, 0.005, 0.004, 0.006, 1.005, 2.505, 3.14159, 100.0]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(f"dollars_to_cents({val}) = {result}")