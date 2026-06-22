def calculate_length_ratio(len1, len2):
    smaller = min(len1, len2)
    larger = max(len1, len2)
    ratio = larger / smaller if smaller != 0 else float('inf')
    return ratio

if __name__ == '__main__':
    length_a = 8
    length_b = 32
    ratio = calculate_length_ratio(length_a, length_b)
    print(ratio)