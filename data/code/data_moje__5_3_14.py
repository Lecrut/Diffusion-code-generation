def compare_lengths(length_a, length_b):
    if length_a > length_b:
        return f"Length A is longer than Length B by {length_a - length_b} units"
    elif length_b > length_a:
        return f"Length B is longer than Length A by {length_b - length_a} units"
    else:
        return "Both lengths are equal"

if __name__ == '__main__':
    length_a = 15.5
    length_b = 12.0
    result = compare_lengths(length_a, length_b)
    print(result)