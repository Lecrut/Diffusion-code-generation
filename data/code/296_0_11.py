def calculate_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return numerator / denominator

if __name__ == '__main__':
    result = calculate_ratio(10, 2)
    print(result)