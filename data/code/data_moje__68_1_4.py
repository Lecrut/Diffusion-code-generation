import decimal

def convert_dollars_to_cents(dollar_value):
    context = decimal.getcontext()
    original_prec = context.prec
    context.prec = 28
    try:
        amount = decimal.Decimal(str(dollar_value))
        multiplier = decimal.Decimal('100')
        cents = amount * multiplier
        return int(cents.to_integral_value(rounding=decimal.ROUND_HALF_UP))
    finally:
        context.prec = original_prec

if __name__ == '__main__':
    sample_values = [10.5, 0.01, 100.00, 12.345, 99.999]
    for val in sample_values:
        result = convert_dollars_to_cents(val)
        print(f"{val} dollars is {result} cents")