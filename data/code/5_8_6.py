def compare_lengths(length1, length2):
    absolute_difference = abs(length1 - length2)
    if length1 == 0 and length2 == 0:
        percentage_difference = 0.0
    elif length1 == 0 or length2 == 0:
        if length1 == 0:
            percentage_difference = float('inf') if length2 != 0 else 0.0
        else:
            percentage_difference = float('inf')
    else:
        percentage_difference = (absolute_difference / ((length1 + length2) / 2)) * 100
    return absolute_difference, percentage_difference
if __name__ == '__main__':
    sample_length1 = 150.5
    sample_length2 = 180.0
    diff, percent = compare_lengths(sample_length1, sample_length2)
    print(f"Length 1: {sample_length1}")
    print(f"Length 2: {sample_length2}")
    print("-" * 30)
    print(f"Absolute Difference: {diff}")
    print(f"Percentage Difference: {percent:.2f}%")