def dollar_to_cents(dollar_amount):
    if not isinstance(dollar_amount, (int, float)):
        raise TypeError("Input must be a number")
    if abs(dollar_amount - round(dollar_amount, 2)) > 1e-9:
        raise ValueError("Input must have at most two decimal places")
    sign = 1 if dollar_amount >= 0 else -1
    abs_dollars = abs(dollar_amount)
    rounded = round(abs_dollars, 2)
    cents = int(rounded * 100)
    return cents * sign

if __name__ == '__main__':
    amount1 = 10.50
    result1 = dollar_to_cents(amount1)
    print(result1)

    amount2 = -3.25
    result2 = dollar_to_cents(amount2)
    print(result2)

    amount3 = 0.00
    result3 = dollar_to_cents(amount3)
    print(result3)