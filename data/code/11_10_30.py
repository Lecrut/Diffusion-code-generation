def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / float(denominator)

if __name__ == '__main__':
    num = 42
    denom = 7
    result = compute_ratio(num, denom)
    print(result)