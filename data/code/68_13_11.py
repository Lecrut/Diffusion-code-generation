def convert_dollars_to_cents(amount):
    return int(amount * 100)

if __name__ == '__main__':
    sample_positive = 12.50
    sample_negative = -5.25
    sample_zero = 0.00
    sample_decimal = 99.99

    print(convert_dollars_to_cents(sample_positive))
    print(convert_dollars_to_cents(sample_negative))
    print(convert_dollars_to_cents(sample_zero))
    print(convert_dollars_to_cents(sample_decimal))