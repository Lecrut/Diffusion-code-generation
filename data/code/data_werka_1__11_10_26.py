def compute_ratio(numerator, denominator):
    try:
        return float(numerator) / denominator
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    numerator = 10
    denominator = 5
    result = compute_ratio(numerator, denominator)
    print(result)