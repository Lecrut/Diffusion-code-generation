def dollars_to_cents(dollars: float | int) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number (int or float).")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a number (int or float).")
    if dollars != dollars:
        raise ValueError("Input must not be NaN.")
    if dollars == float('inf') or dollars == float('-inf'):
        raise ValueError("Input must be finite.")
    cents = round(dollars * 100)
    return cents

if __name__ == '__main__':
    sample_dollars = 12.34
    result = dollars_to_cents(sample_dollars)
    print(result)
    sample_negative = -5.01
    result_neg = dollars_to_cents(sample_negative)
    print(result_neg)
    sample_whole = 10
    result_whole = dollars_to_cents(sample_whole)
    print(result_whole)