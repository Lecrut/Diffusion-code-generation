def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / denominator

if __name__ == '__main__':
    numerator_value = 10
    denominator_value = 3
    result = compute_ratio(numerator_value, denominator_value)
    print(result)