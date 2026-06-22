def calculate_ratio(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator

if __name__ == '__main__':
    sample_numerator = 15
    sample_denominator = 3
    result = calculate_ratio(sample_numerator, sample_denominator)
    print(f"Calculated Ratio: {result}")