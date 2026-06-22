def convert_to_cents(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Input must be a number")
    if amount < 0:
        return -int(abs(amount) * 100)
    return int(amount * 100 + 0.5)

if __name__ == '__main__':
    sample_amount = 123.45
    result = convert_to_cents(sample_amount)
    print(result)
    negative_sample = -10.50
    negative_result = convert_to_cents(negative_sample)
    print(negative_result)