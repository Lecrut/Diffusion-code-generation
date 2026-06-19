def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / float(denominator)

if __name__ == '__main__':
    num = 10
    den = 3
    result = compute_ratio(num, den)
    print(result)