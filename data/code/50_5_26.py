def safe_non_negative_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return abs(a - b)

if __name__ == '__main__':
    sample_values = [100, 50]
    print(safe_non_negative_difference(*sample_values))