def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / denominator

if __name__ == '__main__':
    numerator = 20
    denominator = 7
    result = compute_ratio(numerator, denominator)
    print(result)