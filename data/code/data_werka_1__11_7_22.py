def calculate_length_ratio(length1, length2):
    if length2 == 0:
        return float('inf') if length1 > 0 else float('-inf') if length1 < 0 else float('nan')
    return length1 / length2

if __name__ == '__main__':
    length1 = 10.5
    length2 = 3.2
    ratio = calculate_length_ratio(length1, length2)
    print(ratio)