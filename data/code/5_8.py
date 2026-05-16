def compare_lengths(length1, length2):
    absolute_difference = abs(length1 - length2)
    if length1 != 0 and length2 != 0:
        percentage_difference = (absolute_difference / ((length1 + length2) / 2)) * 100
    elif length1 == 0 and length2 == 0:
        percentage_difference = 0.0
    else:
        percentage_difference = float('inf')
    return absolute_difference, percentage_difference
if __name__ == '__main__':
    sample_length1 = 15.5
    sample_length2 = 22.0
    diff, percent_diff = compare_lengths(sample_length1, sample_length2)
    print(f"Length 1: {sample_length1}")
    print(f"Length 2: {sample_length2}")
    print("-" * 30)
    print(f"Absolute Difference: {diff}")
    print(f"Percentage Difference: {percent_diff:.2f}%")