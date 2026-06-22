def dollars_to_cents(dollars):
    if not isinstance(dollars, (int, float)):
        raise TypeError("dollars must be an integer or float")
    if dollars < 0:
        raise ValueError("dollars must be non-negative")
    cents = int(dollars * 100)
    return cents

if __name__ == '__main__':
    sample_values = [0, 1, 1.5, 10.99, 100, 0.01, 0.005]
    for val in sample_values:
        result = dollars_to_cents(val)
        print(result)