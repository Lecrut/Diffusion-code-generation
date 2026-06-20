def compare_lengths(length_a, length_b):
    if length_a > length_b:
        diff = length_a - length_b
        return f"Length A is longer than Length B by {diff} units"
    elif length_b > length_a:
        diff = length_b - length_a
        return f"Length B is longer than Length A by {diff} units"
    else:
        return "Length A and Length B are equal"

if __name__ == '__main__':
    len_a = 10
    len_b = 7
    result = compare_lengths(len_a, len_b)
    print(result)