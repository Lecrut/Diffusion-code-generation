def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number")
    if dollars < 0:
        raise ValueError("Input must be non-negative")
    return int(dollars * 100)

if __name__ == '__main__':
    sample_amounts = [10.50, 0, 100, -5, 0.01]
    for amount in sample_amounts:
        try:
            result = dollars_to_cents(amount)
            print(result)
        except (TypeError, ValueError) as e:
            print(str(e))