def compute_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return float(numerator) / denominator

if __name__ == '__main__':
    NUM = 25
    DENOM = 7
    try:
        ratio_result = compute_ratio(NUM, DENOM)
        print(ratio_result)
    except ValueError as e:
        print(e)