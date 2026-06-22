def convert_to_cents(dollar_value):
    return int(round(dollar_value * 100))

if __name__ == '__main__':
    sample_value_1 = 1.005
    sample_value_2 = 1.495
    sample_value_3 = 2.125
    print(convert_to_cents(sample_value_1))
    print(convert_to_cents(sample_value_2))
    print(convert_to_cents(sample_value_3))