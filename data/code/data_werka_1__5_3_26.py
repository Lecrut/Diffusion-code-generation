def compare_lengths(length_a, length_b):
    if length_a > length_b:
        difference = length_a - length_b
        return f"Length A is longer than Length B by {difference} units"
    elif length_b > length_a:
        difference = length_b - length_a
        return f"Length B is longer than Length A by {difference} units"
    else:
        return "Length A and Length B are equal"

if __name__ == '__main__':
    length1 = 15
    length2 = 10
    result = compare_lengths(length1, length2)
    print(result)