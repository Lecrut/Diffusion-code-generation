def calculate_length_ratio(length1, length2):
    if length2 == 0:
        return float('inf') if length1 > 0 else float('-inf') if length1 < 0 else float('nan')
    return length1 / length2

if __name__ == '__main__':
    sample_length1 = 7.8
    sample_length2 = 2.4
    ratio = calculate_length_ratio(sample_length1, sample_length2)
    print(ratio)