def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    if isinstance(dollars, float) and (dollars != dollars or dollars == float('inf')):
        raise ValueError("Input must be a valid finite number")
    if dollars < 0:
        raise ValueError("Input must be a non-negative number")
    return int(round(dollars * 100))

if __name__ == "__main__":
    sample_values = [10.0, 5.25, 0.99, 100, 0.0]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(result)