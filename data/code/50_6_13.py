def compute_non_negative_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    sample_values = (10, 5)
    result = compute_non_negative_difference(*sample_values)
    print(result)