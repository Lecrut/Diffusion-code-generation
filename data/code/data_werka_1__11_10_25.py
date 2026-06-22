def compute_ratio(numerator, denominator):
    try:
        result = float(numerator) / denominator
    except ZeroDivisionError:
        return None
    return result
if __name__ == '__main__':
    num = 10
    denom = 5
    ratio = compute_ratio(num, denom)
    print(ratio)