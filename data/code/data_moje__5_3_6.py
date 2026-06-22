def compare_lengths(length_a, length_b):
    if length_a > length_b:
        difference = length_a - length_b
        return f"Length A is longer than Length B by {difference} units"
    elif length_b > length_a:
        difference = length_b - length_a
        return f"Length B is longer than Length A by {difference} units"
    else:
        return "Both lengths are equal"

if __name__ == '__main__':
    sample_length_a = 15
    sample_length_b = 10
    result = compare_lengths(sample_length_a, sample_length_b)
    print(result)