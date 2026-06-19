def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / float(denominator)

if __name__ == '__main__':
    numerator = 10
    denominator = 3
    ratio = compute_ratio(numerator, denominator)
    print(ratio)