def dollars_to_cents(dollars):
    if isinstance(dollars, float):
        integer_part = int(dollars)
        fractional_part = dollars - integer_part
        cents_from_fraction = round(fractional_part * 100)
        return integer_part * 100 + cents_from_fraction
    elif isinstance(dollars, int):
        return dollars * 100
    else:
        raise TypeError("Input must be a number")

if __name__ == '__main__':
    sample_values = [10.99, 0.01, 100.00, 0.10, 1.005, 1.004, -5.50, 0]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)