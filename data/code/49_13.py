def calculate_lengths(length1, length2):
    if length1 == 0 or length2 == 0:
        raise ValueError("Lengths cannot be zero")
    original_lengths = {
        "length1": length1,
        "length2": length2
    }
    if length1 > length2:
        difference = length1 - length2
        ratio = length1 / length2
    else:
        difference = length2 - length1
        ratio = length2 / length1
    result = {
        "original_lengths": original_lengths,
        "difference": difference,
        "ratio": ratio
    }
    return result
if __name__ == '__main__':
    l1 = 20
    l2 = 5
    try:
        output = calculate_lengths(l1, l2)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")