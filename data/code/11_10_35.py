def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / denominator

if __name__ == '__main__':
    num = 10
    denom = 5
    result = compute_ratio(num, denom)
    print(result)