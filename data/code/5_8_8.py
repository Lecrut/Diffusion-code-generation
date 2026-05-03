def compare_lengths(length1, length2):
    absolute_difference = abs(length1 - length2)
    if length1 == 0 and length2 == 0:
        percentage_difference = 0.0
    elif length1 == 0:
        percentage_difference = (absolute_difference / length2) * 100 if length2 != 0 else float('inf')
    elif length2 == 0:
        percentage_difference = (absolute_difference / length1) * 100
    else:
        percentage_difference = (absolute_difference / ((length1 + length2) / 2)) * 100
    return absolute_difference, percentage_difference
if __name__ == '__main__':
    length_a = 15.5
    length_b = 22.0
    diff, percent = compare_lengths(length_a, length_b)
    print("Length Comparison Report")
    print("------------------------")
    print(f"Length 1: {length_a}")
    print(f"Length 2: {length_b}")
    print(f"Absolute Difference: {diff}")
    print(f"Percentage Difference: {percent:.2f}%")