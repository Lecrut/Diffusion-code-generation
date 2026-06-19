def compute_ratio(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(a) / float(b)

if __name__ == '__main__':
    numerator = 10
    denominator = 5
    result = compute_ratio(numerator, denominator)
    print(result)