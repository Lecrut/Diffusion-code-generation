def dollars_to_cents(amount):
    amount_str = str(amount)
    clean_str = amount_str.replace('.', '')
    return int(clean_str)

if __name__ == '__main__':
    sample_value = 12.34
    result = dollars_to_cents(sample_value)
    print(result)
    sample_value_2 = 5.0
    result_2 = dollars_to_cents(sample_value_2)
    print(result_2)
    sample_value_3 = 100.99
    result_3 = dollars_to_cents(sample_value_3)
    print(result_3)