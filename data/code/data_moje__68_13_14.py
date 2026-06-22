def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if dollars < 0:
        return -int(abs(dollars) * 100)
    return int(dollars * 100)

if __name__ == '__main__':
    amount = 12.34
    result = dollars_to_cents(amount)
    print(result)
    negative_amount = -5.67
    negative_result = dollars_to_cents(negative_amount)
    print(negative_result)
    zero_amount = 0.0
    zero_result = dollars_to_cents(zero_amount)
    print(zero_result)