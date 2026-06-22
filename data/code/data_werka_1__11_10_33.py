def compute_ratio(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return float('inf')

if __name__ == '__main__':
    numerator = 42
    denominator = 7
    result = compute_ratio(numerator, denominator)
    print(result)