def compare_lengths(length1, length2):
    absolute_difference = abs(length1 - length2)
    if length1 != 0 and length2 != 0:
        percentage_difference = (absolute_difference / ((length1 + length2) / 2)) * 100
    else:
        percentage_difference = float('inf') if length1 != length2 else 0.0
    return absolute_difference, percentage_difference
if __name__ == '__main__':
    length_a = 15.5
    length_b = 22.0
    diff, percent = compare_lengths(length_a, length_b)
    print(f"Length A: {length_a}")
    print(f"Length B: {length_b}")
    print("-" * 30)
    print(f"Absolute Difference: {diff}")
    print(f"Percentage Difference: {percent:.2f}%")