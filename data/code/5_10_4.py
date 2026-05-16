def compare_lengths(length1, length2):
    if length1 > length2:
        difference = length1 - length2
        result = "greater than"
    elif length1 < length2:
        difference = length2 - length1
        result = "less than"
    else:
        difference = 0
        result = "equal to"
    return difference, result
if __name__ == '__main__':
    a = 15
    b = 25
    diff, comparison = compare_lengths(a, b)
    print(f"Length 1: {a}")
    print(f"Length 2: {b}")
    print(f"Difference: {diff}")
    print(f"Comparison: {comparison}")
    a = 10
    b = 10
    diff, comparison = compare_lengths(a, b)
    print(f"\nLength 1: {a}")
    print(f"Length 2: {b}")
    print(f"Difference: {diff}")
    print(f"Comparison: {comparison}")
    a = 30
    b = 10
    diff, comparison = compare_lengths(a, b)
    print(f"\nLength 1: {a}")
    print(f"Length 2: {b}")
    print(f"Difference: {diff}")
    print(f"Comparison: {comparison}")