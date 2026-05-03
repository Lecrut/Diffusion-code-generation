def calculate_lengths(a, b):
    if a == 0 or b == 0:
        raise ValueError("Input lengths must be non-zero.")
    original_lengths = {
        "length_a": a,
        "length_b": b,
        "difference": abs(a - b),
        "ratio": max(a, b) / min(a, b)
    }
    return original_lengths
if __name__ == '__main__':
    length1 = 10
    length2 = 5
    result = calculate_lengths(length1, length2)
    print(result)