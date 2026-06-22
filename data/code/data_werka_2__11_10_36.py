def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / float(denominator)

if __name__ == '__main__':
    NUMERATOR = 15
    DENOMINATOR = 4
    result = compute_ratio(NUMERATOR, DENOMINATOR)
    print(result)